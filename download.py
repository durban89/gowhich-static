import requests
from bs4 import BeautifulSoup
import markdownify  # 需要安装：pip install markdownify
from datetime import datetime
import argparse

class WebPageAnalyzer:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        """获取网页内容"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # 检查请求是否成功
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return True
        except requests.RequestException as e:
            print(f"请求错误: {e}")
            return False
        except Exception as e:
            print(f"发生未知错误: {e}")
            return False

    def get_title(self):
        """获取页面标题"""
        if self.soup:
            title = self.soup.title
            return title.text if title else "无标题"
        return "页面未加载"

    def count_elements(self, tag_name):
        """计算指定标签的元素数量"""
        if self.soup:
            return len(self.soup.find_all(tag_name))
        return 0

    def find_links(self):
        """查找所有链接"""
        links = []
        if self.soup:
            for link in self.soup.find_all('a'):
                href = link.get('href')
                text = link.get_text(strip=True)
                links.append((href, text))
        return links

    def get_meta_tags(self):
        """获取所有meta标签"""
        meta_tags = []
        if self.soup:
            for meta in self.soup.find_all('meta'):
                meta_tags.append(meta.attrs)
        return meta_tags

    def remove_hidden_elements(self, element):
        """递归移除元素中带有 style='display:none' 的子元素
        
        Args:
            element: BeautifulSoup元素对象
        """
        from bs4 import Tag
        
        # 检查当前元素是否隐藏
        if isinstance(element, Tag) and element.has_attr('style'):
            style = element.get('style', '')
            if 'display:none' in style.lower().replace(' ', ''):
                # 如果当前元素隐藏，则移除整个元素
                element.decompose()
                return None
        
        # 递归处理子元素
        if isinstance(element, Tag):
            for child in list(element.children):  # 使用list()复制列表，避免在迭代时修改
                if isinstance(child, Tag) and child.has_attr('style'):
                    style = child.get('style', '')
                    if 'display:none' in style.lower().replace(' ', ''):
                        # 移除隐藏的子元素
                        child.decompose()
                        continue  # 跳过已移除元素的处理
                
                # 递归处理子元素的子元素
                self.remove_hidden_elements(child)
        
        return element

    def remove_copyright_elements(self, element):
        """移除元素中 class 为 entry-copyright 的子元素
        
        Args:
            element: BeautifulSoup元素对象
        """
        from bs4 import Tag
        
        # 检查当前元素是否是标签
        if isinstance(element, Tag):
            # 查找并移除所有 class 包含 entry-copyright 的子元素
            for child in element.find_all(class_="entry-copyright"):
                child.decompose()
            
            # 递归处理所有子元素
            for child in element.children:
                self.remove_copyright_elements(child)
        
        return element

    def find_elements_by_class(self, class_name, remove_hidden=True, remove_copyright=True):
        """查找具有指定类的所有元素
        
        Args:
            class_name: 要查找的类名
            remove_hidden: 是否移除隐藏元素
            remove_copyright: 是否移除版权元素
        """
        elements = []
        if self.soup:
            elements = self.soup.find_all(class_=class_name)
            
            # 如果需要移除隐藏元素
            if remove_hidden and elements:
                filtered_elements = []
                for element in elements:
                    # 移除隐藏的子元素
                    cleaned_element = self.remove_hidden_elements(element)
                    if cleaned_element:  # 确保元素未被完全移除
                        filtered_elements.append(cleaned_element)
                elements = filtered_elements
            
            # 如果需要移除版权元素
            if remove_copyright and elements:
                remove_elements = []
                for element in elements:
                    removed_element = self.remove_copyright_elements(element)
                    if removed_element:
                        remove_elements.append(removed_element)

                elements = remove_elements
        
        return elements

    def count_elements_by_class(self, class_name):
        """计算具有指定类的元素数量"""
        return len(self.find_elements_by_class(class_name))

    def get_class_elements_info(self, class_name):
        """获取具有指定类的元素的信息"""
        elements_info = []
        for element in self.find_elements_by_class(class_name):
            tag_name = element.name
            text = element.get_text(strip=True)
            attrs = dict(element.attrs)
            elements_info.append({
                'tag': tag_name,
                'text': text,
                'attributes': attrs
            })
        return elements_info
        
    def extract_code_language(self, element):
        """从代码块元素及其子元素中提取语言信息
        
        Args:
            element: BeautifulSoup元素对象
        """
        # 尝试从元素自身的class属性中提取语言
        if element.has_attr('class'):
            classes = element.get('class')
            for cls in classes:
                # 常见的代码语言标记前缀
                if cls.startswith('language-') or cls.startswith('lang-'):
                    return cls.split('-', 1)[1]
                    
                # 直接匹配常见语言名称
                common_languages = [
                    'bash',
                    'objectivec',
                    'python', 'java', 
                    'javascript', 'html', 
                    'css', 'php', 'sql', 
                    'bash', 'json', 'c', 'cpp', 
                    'csharp', 'go', 'rust', 
                    'swift', 'kotlin', 'ruby', 
                    'perl', 'dart', 'scala', 'typescript']
                if cls.lower() in common_languages:
                    return cls.lower()
        
        # 尝试从data-language属性中提取
        if element.has_attr('data-language'):
            return element.get('data-language')
            
        # 尝试从父元素的class中提取
        parent = element.parent
        if parent and parent.has_attr('class'):
            classes = parent.get('class')
            for cls in classes:
                if cls.startswith('language-') or cls.startswith('lang-'):
                    return cls.split('-', 1)[1]
        
        # 尝试从子元素中提取语言信息
        # 特别处理 <pre><code class="language-*">...</code></pre> 结构
        if element.name == 'pre':
            code_elements = element.find_all('code', recursive=False)
            for code in code_elements:
                if code.has_attr('class'):
                    classes = code.get('class')
                    for cls in classes:
                        if cls.startswith('language-') or cls.startswith('lang-'):
                            return cls.split('-', 1)[1]
                            
                        if cls.lower() in common_languages:
                            return cls.lower()
                            
                # 尝试data-language属性
                if code.has_attr('data-language'):
                    return code.get('data-language')
        
        # 尝试从第一个非空文本子元素中提取语言信息
        # 适用于一些markdown渲染器生成的结构
        if element.name == 'pre':
            first_child = next((child for child in element.children if hasattr(child, 'strip') and child.strip()), None)
            if first_child and first_child.strip().startswith(('```', '~~~')):
                # 提取markdown代码块开头的语言标记
                # 例如: ```python 或 ~~~javascript
                code_block_start = first_child.strip()
                for marker in ('```', '~~~'):
                    if code_block_start.startswith(marker):
                        lang_part = code_block_start[len(marker):].strip()
                        if lang_part and ' ' not in lang_part:
                            return lang_part
                            
        return None    

    def html_to_markdown(self, html_content=None, preserve_code_language=True):
        """将HTML内容转换为Markdown格式
        
        Args:
            html_content: 可选的HTML内容，如果未提供则使用当前页面内容
        """
        if html_content is None:
            if self.soup is None:
                print("错误：没有可用的HTML内容，请先调用fetch_page()或提供html_content参数")
                return None
            html_content = str(self.soup)
        
        try:
            # 设置代码语言提取回调函数
            if preserve_code_language:
                markdown = markdownify.markdownify(
                    html_content, 
                    heading_style="ATX",
                    code_language_callback=self.extract_code_language
                )
            else:
                markdown = markdownify.markdownify(html_content, heading_style="ATX")
                
            return markdown
        except Exception as e:
            print(f"HTML转Markdown失败: {e}")
            return None

    def get_element_markdown(self, element, preserve_code_language=True):
        """将单个元素转换为Markdown格式"""
        try:
            # 设置代码语言提取回调函数
            if preserve_code_language:
                return markdownify.markdownify(
                    str(element), 
                    heading_style="ATX",
                    code_language_callback=self.extract_code_language
                )
            else:
                return markdownify.markdownify(str(element), heading_style="ATX")
        except Exception as e:
            print(f"元素转Markdown失败: {e}")
            return None

    def replace_keywords(self, text, replacements=None, max_replacements=10):
        """替换文本中的指定关键词
        
        Args:
            text: 要处理的文本
            replacements: 替换规则字典，默认为常见技术术语的规范化
            max_replacements: 最多替换的关键词数量，默认为10
        """
        if replacements is None:
            replacements = {
                'ios': 'iOS',
                'php': 'PHP',
                'html': 'HTML',
                'css': 'CSS',
                'javascript': 'JavaScript',
                'IOS': 'iOS',
                'sql': 'SQL',
                'mysql': 'MySQL',
                'mongodb': 'MongoDB',
                'yii': 'Yii'
            }
            
        # 限制替换的关键词数量
        if len(replacements) > max_replacements:
            print(f"警告: 替换规则数量超过最大限制({max_replacements})，只使用前{max_replacements}个")
            replacements = {k: replacements[k] for k in list(replacements)[:max_replacements]}
            
        # 使用正则表达式进行关键词替换
        import re
        pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b', re.IGNORECASE)
        
        def replace(match):
            key = match.group(0)
            return replacements.get(key.lower(), key)
            
        return pattern.sub(replace, text)

    def replace_empty_keywords(self, text, replacements=None, max_replacements=10):
        """替换文本中的指定字符
        
        Args:
            text: 要处理的文本
            replacements: 替换规则字典
            max_replacements: 最多替换的规则数量，默认为10
        """
        if replacements is None:
            replacements = {
                '、': '-',
                '）': '-',
                '（': '-',
                ')': '-',
                '(': '-',
                '，': '-',
                ',': '-',
                '&quot;': '-',
                '“': '-',
                '”': '-',
                ' ': '-',
                '/': '-',
                '#': '井'
            }
            
        # 限制替换的规则数量
        if len(replacements) > max_replacements:
            print(f"警告: 替换规则数量超过最大限制({max_replacements})，只使用前{max_replacements}个")
            replacements = {k: replacements[k] for k in list(replacements)[:max_replacements]}
        
        # 先处理空格，将连续空格合并为单个连字符
        if ' ' in replacements:
            text = text.replace(' ', replacements[' '])
            # 合并连续的连字符
            while replacements[' '] * 2 in text:
                text = text.replace(replacements[' '] * 2, replacements[' '])
        
        # 处理其他替换规则
        for old_char, new_char in replacements.items():
            if old_char != ' ':  # 跳过已处理的空格
                text = text.replace(old_char, new_char)
        
        return text

    def clean_title(self, title):
        """清理标题，移除末尾的连字符和多余空格
        
        Args:
            title: 原始标题字符串
        """
        # 移除末尾的所有连字符和空格
        cleaned_title = title.rstrip('- ').lstrip()
        
        # 如果标题为空，返回默认值
        return cleaned_title if cleaned_title else "未命名文章"

    def generate_front_matter(self, title="默认标题", categories=None, tags=None):
        """生成Markdown文件的前置元数据
        
        Args:
            title: 文章标题
            categories: 文章分类列表
            tags: 文章标签列表
        """
        if categories is None:
            categories = ["技术"]
        if tags is None:
            tags = ["PHP"]
            
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        title = title.split('|')[0].split(' - ')[0].split(':')[0].strip()

        title = self.replace_keywords(title)

        front_matter = f"""---
title: {title}
tags:
  - PHP
categories:
  - 技术
date: {current_time}
---
"""
        return front_matter

    def save_markdown_to_file(self, markdown_content, file_path, encoding='utf-8', add_front_matter=True):
        """将Markdown内容保存到文件
        
        Args:
            markdown_content: 要保存的Markdown内容
            file_path: 保存文件的路径
            encoding: 文件编码，默认为utf-8
            add_front_matter: 是否添加前置元数据
        """
        if not markdown_content:
            print("错误：没有Markdown内容可保存")
            return False
            
        try:
            # 如果需要添加前置元数据
            if add_front_matter:
                # 获取页面标题作为文章标题
                page_title = self.get_title()
                # 生成前置元数据
                front_matter = self.generate_front_matter(title=page_title)
                # 合并前置元数据和Markdown内容
                content_to_save = front_matter + "\n" + markdown_content
            else:
                content_to_save = markdown_content
                
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(content_to_save)
            print(f"Markdown内容已成功保存到 {file_path}")
            return True
        except Exception as e:
            print(f"保存文件失败: {e}")
            return False

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='网页内容分析工具')
    
    # 添加必需的URL参数
    parser.add_argument('url', type=str, help='目标网页的URL')

    # 解析命令行参数
    args = parser.parse_args()
    
    print(f"目标URL: {args.url}")

    target_url = args.url # "https://www.gowhich.com/blog/60"
    target_class = "shapely-content dropcaps-content"
    output_file = "blog_content.md"
    
    analyzer = WebPageAnalyzer(target_url)
    if analyzer.fetch_page():
        title = analyzer.get_title().split('|')[0].split(' - ')[0].split(':')[0].strip()
        title = analyzer.replace_keywords(title)
        title = analyzer.replace_empty_keywords(title)
        title = analyzer.clean_title(title)

        output_file = f"./source/_posts/{title}.md"
        print(f"页面标题: {analyzer.get_title()}")
        print(f"页面总链接数: {analyzer.count_elements('a')}")
        
        # 测试获取指定class的元素
        print(f"\n查找class为 '{target_class}' 的元素:")
        elements = analyzer.find_elements_by_class(target_class)
        
        if elements:
            print(f"找到 {len(elements)} 个匹配的元素")
            
            # 获取第一个匹配元素的Markdown格式
            first_element = elements[0]
            element_md = analyzer.get_element_markdown(
                first_element,
                preserve_code_language=True)
            
            if element_md:
                # 保存Markdown到文件（默认添加前置元数据）
                if analyzer.save_markdown_to_file(element_md, output_file):
                    print(f"已将第一个匹配元素的Markdown内容保存到 {output_file}")
                    
                    # 显示保存的内容预览（包括前置元数据）
                    print("\n保存内容预览:")
                    with open(output_file, 'r', encoding='utf-8') as f:
                        preview = f.read(500)
                        print(preview + ("..." if len(preview) == 500 else ""))
            else:
                print("无法将元素转换为Markdown格式")
        else:
            print(f"未找到class为 '{target_class}' 的元素")
            
