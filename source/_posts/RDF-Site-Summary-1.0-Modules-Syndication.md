---
title: "RDF Site Summary 1.0 Modules: Syndication（RSS联合模块）"
tags:
  - RSS
categories:
  - 技术
date: 2025-06-12 11:49:47
---

RDF Site Summary 1.0 Modules: Syndication

举个例子:

```xml
<?xml version="1.0" encoding="utf-8"?> 

<rdf:RDF 
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
  xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
  xmlns="http://purl.org/rss/1.0/"
> 

  <channel rdf:about="http://meerkat.oreillynet.com/?_fl=rss1.0">
    <title>Meerkat</title>
    <link>http://meerkat.oreillynet.com</link>
    <description>Meerkat: An Open Wire Service</description>
    <sy:updatePeriod>hourly</sy:updatePeriod>
    <sy:updateFrequency>2</sy:updateFrequency>
    <sy:updateBase>2000-01-01T12:00+00:00</sy:updateBase>

    <image rdf:resource="http://meerkat.oreillynet.com/icons/meerkat-powered.jpg" />

    <items>
      <rdf:Seq>
        <rdf:li resource="http://c.moreover.com/click/here.pl?r123" />
      </rdf:Seq>
    </items>

    <textinput rdf:resource="http://meerkat.oreillynet.com" />

  </channel>

  <image rdf:about="http://meerkat.oreillynet.com/icons/meerkat-powered.jpg">
    <title>Meerkat Powered!</title>
    <url>http://meerkat.oreillynet.com/icons/meerkat-powered.jpg</url>
    <link>http://meerkat.oreillynet.com</link>
  </image>

  <item rdf:about="http://c.moreover.com/click/here.pl?r123">
    <title>XML: A Disruptive Technology</title> 
    <link>http://c.moreover.com/click/here.pl?r123</link>
    <description>
      XML is placing increasingly heavy loads on the existing technical
      infrastructure of the Internet.
    </description>
  </item> 

  <textinput rdf:about="http://meerkat.oreillynet.com">
    <title>Search Meerkat</title>
    <description>Search Meerkat's RSS Database...</description>
    <name>s</name>
    <link>http://meerkat.oreillynet.com/</link>
  </textinput>

</rdf:RDF>
```
