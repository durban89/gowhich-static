---
title: Nodejs搭建web服务器
tags:
  - Nodejs
categories:
  - 技术
date: 2025-06-10 10:40:46
---
nodejs的安装其实是很简单的，官方文档是有直接安装的文件的，之后linux下的稍微麻烦一点，不过只要解压一下，然后直接安装，也是比较简单的。

如果不懂的可以参考我的这篇文章[nodejs的安装，测试，hello world](https://www.gowhich.com/blog/40) 

下面演示我的web服务器

第一个是引导文件：

直接看代码好了

index.js

```javascript
var server = require('./server');
var router = require('./router');
var requestHandlers = require('./requestHandlers');
var handle = {};
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/weibo"] = requestHandlers.weibo;
handle["/baiduindex"] = requestHandlers.baiduindex;
server.start(router.route,handle);
```

看到上面的代码中，require了三个文件，下面我分别给出这三个文件

server.js

```javascript
var http = require('http');
var url = require('url');
var querystring = require("querystring");
function start(route,handle){
  function onRequest(request,response){
    var url_array = url.parse(request.url,true);
    var pathname = url_array.pathname;
    var query_param = url_array.query;
        
    route(handle, pathname, response, query_param);
  }
  http.createServer(onRequest).listen(8006);
  console.log("Server has started. listen:8006");
}
exports.start = start;
```

router.js

```javascript
function route(handle,pathname, response, query_param){
//  console.log("About to route a request for "+pathname);
  if(typeof handle[pathname] === "function"){
    return handle[pathname](response, query_param);
  }else{
//    console.log("No request handler found for " + pathname);
      response.writeHead(404, {"Content-Type": "text/plain"});
      response.write("404 Not found");
      response.end();
  }
}
exports.route = route;
```

requestHandlers.js

```javascript
var querystring = require("querystring");
var sinaweibo = require("./sinaWeibo");
var baidu = require("./baiduIndex");

function start(response, query_param){
//  console.log("Request handler 'start' was called.");
  return "Hello Start";
}

function upload(response, query_param){
//  console.log("Request handler 'upload' was called.");
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("You've sent: " + postData +"  " + querystring.parse(postData).text);
  response.end();
}

function weibo(response, query_param){
  var content = sinaweibo.GetRSA(query_param.servertime,query_param.nonce,query_param.password);
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write(content);
  response.end();
}
function baiduindex(response, query_param){
  var content = baidu.execEval(query_param.input,query_param.key);
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write(content);
  response.end();
}
exports.start = start;
exports.upload = upload;
exports.weibo = weibo;
exports.baiduindex = baiduindex;
```

在requestHandlers.js文件中，又引入了两个文件，分别是关于sinaWeibo和baiduIndex

在这两个文件中分别是关于对应的一个操作，如果你要针对于自己的操作，也可以自己加入到里面来。

sinaWeibo.js

```javascript
var sinaSSOEncoder = sinaSSOEncoder || {};
(function(){
 var hexcase =   0;
 var chrsz = 8; 
 this.hex_sha1 = function(s){return   binb2hex(core_sha1(str2binb(s),s.length * chrsz));}; 
 var core_sha1 = function(x, len) {    
 x[len >> 5] |= 0x80 << (24 - len % 32);   
 x[((len + 64 >> 9) << 4) + 15] = len;   
 var w = Array(80); 
 var a =   1732584193; 
 var b = -271733879; 
 var c = -1732584194; 
 var d =   271733878; 
 var e = -1009589776; 

 for(var i = 0; i < x.length; i += 16) { 
   var olda = a; 
   var oldb = b; 
   var oldc = c; 
   var oldd = d; 
   var olde = e; 

   for(var j = 0; j < 80; j++) { 
   if(j < 16) w[j] = x[i + j]; 
   else w[j] = rol(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1); 
   var t = safe_add(safe_add(rol(a, 5), sha1_ft(j, b, c, d)),   
       safe_add(safe_add(e, w[j]), sha1_kt(j))); 
   e = d; 
   d = c; 
   c = rol(b, 30); 
   b = a; 
   a = t; 
   } 

   a = safe_add(a, olda); 
   b = safe_add(b, oldb); 
   c = safe_add(c, oldc); 
   d = safe_add(d, oldd); 
   e = safe_add(e, olde); 
 } 
 return Array(a, b, c, d, e);   

 };
 /* 
  * Perform the appropriate triplet combination function for the current 
  * iteration 
  */ 
 var sha1_ft = function(t, b, c, d) { 
   if(t < 20) return (b & c) | ((~b) & d); 
   if(t < 40) return b ^ c ^ d; 
   if(t < 60) return (b & c) | (b & d) | (c & d); 
   return b ^ c ^ d; 
 }; 

 /* 
  * Determine the appropriate additive constant for the current iteration 
  */ 
 var sha1_kt = function(t) { 
   return (t < 20) ?   1518500249 : (t < 40) ?   1859775393 : 
   (t < 60) ? -1894007588 : -899497514; 
 };  
 /* 
  * Add integers, wrapping at 2^32. This uses 16-bit operations internally 
  * to work around bugs in some JS interpreters. 
  */ 
 var safe_add = function(x, y) { 
   var lsw = (x & 0xFFFF) + (y & 0xFFFF); 
   var msw = (x >> 16) + (y >> 16) + (lsw >> 16); 
   return (msw << 16) | (lsw & 0xFFFF); 
 };  

 /* 
  * Bitwise rotate a 32-bit number to the left. 
  */ 
 var rol = function(num, cnt) { 
   return (num << cnt) | (num >>> (32 - cnt)); 
 };  

 var str2binb = function(str) {   
   var bin = Array();   
   var mask = (1 << chrsz) - 1;
   for(var i = 0; i < str.length * chrsz; i += chrsz)
     bin[i>>5] |= (str.charCodeAt(i /chrsz) & mask) << (24 - i%32);
   return   bin;     
 };
 var binb2hex = function(binarray) {   
   var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";   
   var str = "";   
   for(var i = 0; i < binarray.length * 4; i++){   
     str += hex_tab.charAt((binarray[i>>2] >> ((3 - i%4)*8+4)) & 0xF) +   
       hex_tab.charAt((binarray[i>>2] >> ((3 - i%4)*8 )) & 0xF);   
   }   
   return str;   
 };

 this.base64 = {
  encode:function(input) {
    input = "" + input; // Convert to string for encode
    if (input == "") return ""; 
  
    var output = '';
    var chr1, chr2, chr3 = '';
    var enc1, enc2, enc3, enc4 = '';
    var i = 0;
    do {
      chr1 = input.charCodeAt(i++);
      chr2 = input.charCodeAt(i++);
      chr3 = input.charCodeAt(i++);
      enc1 = chr1 >> 2;
      enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
      enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
      enc4 = chr3 & 63;
      if (isNaN(chr2)){
        enc3 = enc4 = 64;
      } else if (isNaN(chr3)){
        enc4 = 64;
      }
      output = output+this._keys.charAt(enc1)+this._keys.charAt(enc2)+this._keys.charAt(enc3)+this._keys.charAt(enc4);
      chr1 = chr2 = chr3 = '';
      enc1 = enc2 = enc3 = enc4 = '';
    } while (i < input.length);
    return output;
  },
  
  _keys: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

 };
}).call(sinaSSOEncoder);

//RSA
;(function(){ 
  /********************* jsbn.js start ************************/

  // Copyright (c) 2005  Tom Wu
  // All Rights Reserved.
  // See "LICENSE" for details.
  
  // Basic JavaScript BN library - subset useful for RSA encryption.
  
  // Bits per digit
  var dbits;
  
  // JavaScript engine analysis
  var canary = 0xdeadbeefcafe;
  var j_lm = ((canary&0xffffff)==0xefcafe);
  
  // (public) Constructor
  function BigInteger(a,b,c) {
    if(a != null)
    if("number" == typeof a) this.fromNumber(a,b,c);
    else if(b == null && "string" != typeof a) this.fromString(a,256);
    else this.fromString(a,b);
  }
  
  // return new, unset BigInteger
  function nbi() { return new BigInteger(null); }
  
  // am: Compute w_j += (x*this_i), propagate carries,
  // c is initial carry, returns final carry.
  // c < 3*dvalue, x < 2*dvalue, this_i < dvalue
  // We need to select the fastest one that works in this environment.
  
  // am1: use a single mult and divide to get the high bits,
  // max digit bits should be 26 because
  // max internal value = 2*dvalue^2-2*dvalue (< 2^53)
  function am1(i,x,w,j,c,n) {
    while(--n >= 0) {
    var v = x*this[i++]+w[j]+c;
    c = Math.floor(v/0x4000000);
    w[j++] = v&0x3ffffff;
    }
    return c;
  }
  // am2 avoids a big mult-and-extract completely.
  // Max digit bits should be <= 30 because we do bitwise ops
  // on values up to 2*hdvalue^2-hdvalue-1 (< 2^31)
  function am2(i,x,w,j,c,n) {
    var xl = x&0x7fff, xh = x>>15;
    while(--n >= 0) {
    var l = this[i]&0x7fff;
    var h = this[i++]>>15;
    var m = xh*l+h*xl;
    l = xl*l+((m&0x7fff)<<15)+w[j]+(c&0x3fffffff);
    c = (l>>>30)+(m>>>15)+xh*h+(c>>>30);
    w[j++] = l&0x3fffffff;
    }
    return c;
  }
  // Alternately, set max digit bits to 28 since some
  // browsers slow down when dealing with 32-bit numbers.
  function am3(i,x,w,j,c,n) {
    var xl = x&0x3fff, xh = x>>14;
    while(--n >= 0) {
    var l = this[i]&0x3fff;
    var h = this[i++]>>14;
    var m = xh*l+h*xl;
    l = xl*l+((m&0x3fff)<<14)+w[j]+c;
    c = (l>>28)+(m>>14)+xh*h;
    w[j++] = l&0xfffffff;
    }
    return c;
  }
   // Mozilla/Netscape seems to prefer am3
    BigInteger.prototype.am = am3;
    dbits = 28;
  
  
  BigInteger.prototype.DB = dbits;
  BigInteger.prototype.DM = ((1<<dbits)-1);
  BigInteger.prototype.DV = (1<<dbits);
  
  var BI_FP = 52;
  BigInteger.prototype.FV = Math.pow(2,BI_FP);
  BigInteger.prototype.F1 = BI_FP-dbits;
  BigInteger.prototype.F2 = 2*dbits-BI_FP;
  
  // Digit conversions
  var BI_RM = "0123456789abcdefghijklmnopqrstuvwxyz";
  var BI_RC = new Array();
  var rr,vv;
  rr = "0".charCodeAt(0);
  for(vv = 0; vv <= 9; ++vv) BI_RC[rr++] = vv;
  rr = "a".charCodeAt(0);
  for(vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
  rr = "A".charCodeAt(0);
  for(vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
  
  function int2char(n) { return BI_RM.charAt(n); }
  function intAt(s,i) {
    var c = BI_RC[s.charCodeAt(i)];
    return (c==null)?-1:c;
  }
  
  // (protected) copy this to r
  function bnpCopyTo(r) {
    for(var i = this.t-1; i >= 0; --i) r[i] = this[i];
    r.t = this.t;
    r.s = this.s;
  }
  
  // (protected) set from integer value x, -DV <= x < DV
  function bnpFromInt(x) {
    this.t = 1;
    this.s = (x<0)?-1:0;
    if(x > 0) this[0] = x;
    else if(x < -1) this[0] = x+DV;
    else this.t = 0;
  }
  
  // return bigint initialized to value
  function nbv(i) { var r = nbi(); r.fromInt(i); return r; }
  
  // (protected) set from string and radix
  function bnpFromString(s,b) {
    var k;
    if(b == 16) k = 4;
    else if(b == 8) k = 3;
    else if(b == 256) k = 8; // byte array
    else if(b == 2) k = 1;
    else if(b == 32) k = 5;
    else if(b == 4) k = 2;
    else { this.fromRadix(s,b); return; }
    this.t = 0;
    this.s = 0;
    var i = s.length, mi = false, sh = 0;
    while(--i >= 0) {
    var x = (k==8)?s[i]&0xff:intAt(s,i);
    if(x < 0) {
      if(s.charAt(i) == "-") mi = true;
      continue;
    }
    mi = false;
    if(sh == 0)
      this[this.t++] = x;
    else if(sh+k > this.DB) {
      this[this.t-1] |= (x&((1<<(this.DB-sh))-1))<<sh;
      this[this.t++] = (x>>(this.DB-sh));
    }
    else
      this[this.t-1] |= x<<sh;
    sh += k;
    if(sh >= this.DB) sh -= this.DB;
    }
    if(k == 8 && (s[0]&0x80) != 0) {
    this.s = -1;
    if(sh > 0) this[this.t-1] |= ((1<<(this.DB-sh))-1)<<sh;
    }
    this.clamp();
    if(mi) BigInteger.ZERO.subTo(this,this);
  }
  
  // (protected) clamp off excess high words
  function bnpClamp() {
    var c = this.s&this.DM;
    while(this.t > 0 && this[this.t-1] == c) --this.t;
  }
  
  // (public) return string representation in given radix
  function bnToString(b) {
    if(this.s < 0) return "-"+this.negate().toString(b);
    var k;
    if(b == 16) k = 4;
    else if(b == 8) k = 3;
    else if(b == 2) k = 1;
    else if(b == 32) k = 5;
    else if(b == 4) k = 2;
    else return this.toRadix(b);
    var km = (1<<k)-1, d, m = false, r = "", i = this.t;
    var p = this.DB-(i*this.DB)%k;
    if(i-- > 0) {
    if(p < this.DB && (d = this[i]>>p) > 0) { m = true; r = int2char(d); }
    while(i >= 0) {
      if(p < k) {
      d = (this[i]&((1<<p)-1))<<(k-p);
      d |= this[--i]>>(p+=this.DB-k);
      }
      else {
      d = (this[i]>>(p-=k))&km;
      if(p <= 0) { p += this.DB; --i; }
      }
      if(d > 0) m = true;
      if(m) r += int2char(d);
    }
    }
    return m?r:"0";
  }
  
  // (public) -this
  function bnNegate() { var r = nbi(); BigInteger.ZERO.subTo(this,r); return r; }
  
  // (public) |this|
  function bnAbs() { return (this.s<0)?this.negate():this; }
  
  // (public) return + if this > a, - if this < a, 0 if equal
  function bnCompareTo(a) {
    var r = this.s-a.s;
    if(r != 0) return r;
    var i = this.t;
    r = i-a.t;
    if(r != 0) return r;
    while(--i >= 0) if((r=this[i]-a[i]) != 0) return r;
    return 0;
  }
  
  // returns bit length of the integer x
  function nbits(x) {
    var r = 1, t;
    if((t=x>>>16) != 0) { x = t; r += 16; }
    if((t=x>>8) != 0) { x = t; r += 8; }
    if((t=x>>4) != 0) { x = t; r += 4; }
    if((t=x>>2) != 0) { x = t; r += 2; }
    if((t=x>>1) != 0) { x = t; r += 1; }
    return r;
  }
  
  // (public) return the number of bits in "this"
  function bnBitLength() {
    if(this.t <= 0) return 0;
    return this.DB*(this.t-1)+nbits(this[this.t-1]^(this.s&this.DM));
  }
  
  // (protected) r = this << n*DB
  function bnpDLShiftTo(n,r) {
    var i;
    for(i = this.t-1; i >= 0; --i) r[i+n] = this[i];
    for(i = n-1; i >= 0; --i) r[i] = 0;
    r.t = this.t+n;
    r.s = this.s;
  }
  
  // (protected) r = this >> n*DB
  function bnpDRShiftTo(n,r) {
    for(var i = n; i < this.t; ++i) r[i-n] = this[i];
    r.t = Math.max(this.t-n,0);
    r.s = this.s;
  }
  
  // (protected) r = this << n
  function bnpLShiftTo(n,r) {
    var bs = n%this.DB;
    var cbs = this.DB-bs;
    var bm = (1<<cbs)-1;
    var ds = Math.floor(n/this.DB), c = (this.s<<bs)&this.DM, i;
    for(i = this.t-1; i >= 0; --i) {
    r[i+ds+1] = (this[i]>>cbs)|c;
    c = (this[i]&bm)<<bs;
    }
    for(i = ds-1; i >= 0; --i) r[i] = 0;
    r[ds] = c;
    r.t = this.t+ds+1;
    r.s = this.s;
    r.clamp();
  }
  
  // (protected) r = this >> n
  function bnpRShiftTo(n,r) {
    r.s = this.s;
    var ds = Math.floor(n/this.DB);
    if(ds >= this.t) { r.t = 0; return; }
    var bs = n%this.DB;
    var cbs = this.DB-bs;
    var bm = (1<<bs)-1;
    r[0] = this[ds]>>bs;
    for(var i = ds+1; i < this.t; ++i) {
    r[i-ds-1] |= (this[i]&bm)<<cbs;
    r[i-ds] = this[i]>>bs;
    }
    if(bs > 0) r[this.t-ds-1] |= (this.s&bm)<<cbs;
    r.t = this.t-ds;
    r.clamp();
  }
  
  // (protected) r = this - a
  function bnpSubTo(a,r) {
    var i = 0, c = 0, m = Math.min(a.t,this.t);
    while(i < m) {
    c += this[i]-a[i];
    r[i++] = c&this.DM;
    c >>= this.DB;
    }
    if(a.t < this.t) {
    c -= a.s;
    while(i < this.t) {
      c += this[i];
      r[i++] = c&this.DM;
      c >>= this.DB;
    }
    c += this.s;
    }
    else {
    c += this.s;
    while(i < a.t) {
      c -= a[i];
      r[i++] = c&this.DM;
      c >>= this.DB;
    }
    c -= a.s;
    }
    r.s = (c<0)?-1:0;
    if(c < -1) r[i++] = this.DV+c;
    else if(c > 0) r[i++] = c;
    r.t = i;
    r.clamp();
  }
  
  // (protected) r = this * a, r != this,a (HAC 14.12)
  // "this" should be the larger one if appropriate.
  function bnpMultiplyTo(a,r) {
    var x = this.abs(), y = a.abs();
    var i = x.t;
    r.t = i+y.t;
    while(--i >= 0) r[i] = 0;
    for(i = 0; i < y.t; ++i) r[i+x.t] = x.am(0,y[i],r,i,0,x.t);
    r.s = 0;
    r.clamp();
    if(this.s != a.s) BigInteger.ZERO.subTo(r,r);
  }
  
  // (protected) r = this^2, r != this (HAC 14.16)
  function bnpSquareTo(r) {
    var x = this.abs();
    var i = r.t = 2*x.t;
    while(--i >= 0) r[i] = 0;
    for(i = 0; i < x.t-1; ++i) {
    var c = x.am(i,x[i],r,2*i,0,1);
    if((r[i+x.t]+=x.am(i+1,2*x[i],r,2*i+1,c,x.t-i-1)) >= x.DV) {
      r[i+x.t] -= x.DV;
      r[i+x.t+1] = 1;
    }
    }
    if(r.t > 0) r[r.t-1] += x.am(i,x[i],r,2*i,0,1);
    r.s = 0;
    r.clamp();
  }
  
  // (protected) divide this by m, quotient and remainder to q, r (HAC 14.20)
  // r != q, this != m.  q or r may be null.
  function bnpDivRemTo(m,q,r) {
    var pm = m.abs();
    if(pm.t <= 0) return;
    var pt = this.abs();
    if(pt.t < pm.t) {
    if(q != null) q.fromInt(0);
    if(r != null) this.copyTo(r);
    return;
    }
    if(r == null) r = nbi();
    var y = nbi(), ts = this.s, ms = m.s;
    var nsh = this.DB-nbits(pm[pm.t-1]);  // normalize modulus
    if(nsh > 0) { pm.lShiftTo(nsh,y); pt.lShiftTo(nsh,r); }
    else { pm.copyTo(y); pt.copyTo(r); }
    var ys = y.t;
    var y0 = y[ys-1];
    if(y0 == 0) return;
    var yt = y0*(1<<this.F1)+((ys>1)?y[ys-2]>>this.F2:0);
    var d1 = this.FV/yt, d2 = (1<<this.F1)/yt, e = 1<<this.F2;
    var i = r.t, j = i-ys, t = (q==null)?nbi():q;
    y.dlShiftTo(j,t);
    if(r.compareTo(t) >= 0) {
    r[r.t++] = 1;
    r.subTo(t,r);
    }
    BigInteger.ONE.dlShiftTo(ys,t);
    t.subTo(y,y); // "negative" y so we can replace sub with am later
    while(y.t < ys) y[y.t++] = 0;
    while(--j >= 0) {
    // Estimate quotient digit
    var qd = (r[--i]==y0)?this.DM:Math.floor(r[i]*d1+(r[i-1]+e)*d2);
    if((r[i]+=y.am(0,qd,r,j,0,ys)) < qd) {  // Try it out
      y.dlShiftTo(j,t);
      r.subTo(t,r);
      while(r[i] < --qd) r.subTo(t,r);
    }
    }
    if(q != null) {
    r.drShiftTo(ys,q);
    if(ts != ms) BigInteger.ZERO.subTo(q,q);
    }
    r.t = ys;
    r.clamp();
    if(nsh > 0) r.rShiftTo(nsh,r);  // Denormalize remainder
    if(ts < 0) BigInteger.ZERO.subTo(r,r);
  }
  
  // (public) this mod a
  function bnMod(a) {
    var r = nbi();
    this.abs().divRemTo(a,null,r);
    if(this.s < 0 && r.compareTo(BigInteger.ZERO) > 0) a.subTo(r,r);
    return r;
  }
  
  // Modular reduction using "classic" algorithm
  function Classic(m) { this.m = m; }
  function cConvert(x) {
    if(x.s < 0 || x.compareTo(this.m) >= 0) return x.mod(this.m);
    else return x;
  }
  function cRevert(x) { return x; }
  function cReduce(x) { x.divRemTo(this.m,null,x); }
  function cMulTo(x,y,r) { x.multiplyTo(y,r); this.reduce(r); }
  function cSqrTo(x,r) { x.squareTo(r); this.reduce(r); }
  
  Classic.prototype.convert = cConvert;
  Classic.prototype.revert = cRevert;
  Classic.prototype.reduce = cReduce;
  Classic.prototype.mulTo = cMulTo;
  Classic.prototype.sqrTo = cSqrTo;
  
  // (protected) return "-1/this % 2^DB"; useful for Mont. reduction
  // justification:
  //         xy == 1 (mod m)
  //         xy =  1+km
  //   xy(2-xy) = (1+km)(1-km)
  // x[y(2-xy)] = 1-k^2m^2
  // x[y(2-xy)] == 1 (mod m^2)
  // if y is 1/x mod m, then y(2-xy) is 1/x mod m^2
  // should reduce x and y(2-xy) by m^2 at each step to keep size bounded.
  // JS multiply "overflows" differently from C/C++, so care is needed here.
  function bnpInvDigit() {
    if(this.t < 1) return 0;
    var x = this[0];
    if((x&1) == 0) return 0;
    var y = x&3;    // y == 1/x mod 2^2
    y = (y*(2-(x&0xf)*y))&0xf;  // y == 1/x mod 2^4
    y = (y*(2-(x&0xff)*y))&0xff;  // y == 1/x mod 2^8
    y = (y*(2-(((x&0xffff)*y)&0xffff)))&0xffff; // y == 1/x mod 2^16
    // last step - calculate inverse mod DV directly;
    // assumes 16 < DB <= 32 and assumes ability to handle 48-bit ints
    y = (y*(2-x*y%this.DV))%this.DV;    // y == 1/x mod 2^dbits
    // we really want the negative inverse, and -DV < y < DV
    return (y>0)?this.DV-y:-y;
  }
  
  // Montgomery reduction
  function Montgomery(m) {
    this.m = m;
    this.mp = m.invDigit();
    this.mpl = this.mp&0x7fff;
    this.mph = this.mp>>15;
    this.um = (1<<(m.DB-15))-1;
    this.mt2 = 2*m.t;
  }
  
  // xR mod m
  function montConvert(x) {
    var r = nbi();
    x.abs().dlShiftTo(this.m.t,r);
    r.divRemTo(this.m,null,r);
    if(x.s < 0 && r.compareTo(BigInteger.ZERO) > 0) this.m.subTo(r,r);
    return r;
  }
  
  // x/R mod m
  function montRevert(x) {
    var r = nbi();
    x.copyTo(r);
    this.reduce(r);
    return r;
  }
  
  // x = x/R mod m (HAC 14.32)
  function montReduce(x) {
    while(x.t <= this.mt2)  // pad x so am has enough room later
    x[x.t++] = 0;
    for(var i = 0; i < this.m.t; ++i) {
    // faster way of calculating u0 = x[i]*mp mod DV
    var j = x[i]&0x7fff;
    var u0 = (j*this.mpl+(((j*this.mph+(x[i]>>15)*this.mpl)&this.um)<<15))&x.DM;
    // use am to combine the multiply-shift-add into one call
    j = i+this.m.t;
    x[j] += this.m.am(0,u0,x,i,0,this.m.t);
    // propagate carry
    while(x[j] >= x.DV) { x[j] -= x.DV; x[++j]++; }
    }
    x.clamp();
    x.drShiftTo(this.m.t,x);
    if(x.compareTo(this.m) >= 0) x.subTo(this.m,x);
  }
  
  // r = "x^2/R mod m"; x != r
  function montSqrTo(x,r) { x.squareTo(r); this.reduce(r); }
  
  // r = "xy/R mod m"; x,y != r
  function montMulTo(x,y,r) { x.multiplyTo(y,r); this.reduce(r); }
  
  Montgomery.prototype.convert = montConvert;
  Montgomery.prototype.revert = montRevert;
  Montgomery.prototype.reduce = montReduce;
  Montgomery.prototype.mulTo = montMulTo;
  Montgomery.prototype.sqrTo = montSqrTo;
  
  // (protected) true iff this is even
  function bnpIsEven() { return ((this.t>0)?(this[0]&1):this.s) == 0; }
  
  // (protected) this^e, e < 2^32, doing sqr and mul with "r" (HAC 14.79)
  function bnpExp(e,z) {
    if(e > 0xffffffff || e < 1) return BigInteger.ONE;
    var r = nbi(), r2 = nbi(), g = z.convert(this), i = nbits(e)-1;
    g.copyTo(r);
    while(--i >= 0) {
    z.sqrTo(r,r2);
    if((e&(1<<i)) > 0) z.mulTo(r2,g,r);
    else { var t = r; r = r2; r2 = t; }
    }
    return z.revert(r);
  }
  
  // (public) this^e % m, 0 <= e < 2^32
  function bnModPowInt(e,m) {
    var z;
    if(e < 256 || m.isEven()) z = new Classic(m); else z = new Montgomery(m);
    return this.exp(e,z);
  }
  
  // protected
  BigInteger.prototype.copyTo = bnpCopyTo;
  BigInteger.prototype.fromInt = bnpFromInt;
  BigInteger.prototype.fromString = bnpFromString;
  BigInteger.prototype.clamp = bnpClamp;
  BigInteger.prototype.dlShiftTo = bnpDLShiftTo;
  BigInteger.prototype.drShiftTo = bnpDRShiftTo;
  BigInteger.prototype.lShiftTo = bnpLShiftTo;
  BigInteger.prototype.rShiftTo = bnpRShiftTo;
  BigInteger.prototype.subTo = bnpSubTo;
  BigInteger.prototype.multiplyTo = bnpMultiplyTo;
  BigInteger.prototype.squareTo = bnpSquareTo;
  BigInteger.prototype.divRemTo = bnpDivRemTo;
  BigInteger.prototype.invDigit = bnpInvDigit;
  BigInteger.prototype.isEven = bnpIsEven;
  BigInteger.prototype.exp = bnpExp;
  
  // public
  BigInteger.prototype.toString = bnToString;
  BigInteger.prototype.negate = bnNegate;
  BigInteger.prototype.abs = bnAbs;
  BigInteger.prototype.compareTo = bnCompareTo;
  BigInteger.prototype.bitLength = bnBitLength;
  BigInteger.prototype.mod = bnMod;
  BigInteger.prototype.modPowInt = bnModPowInt;
  
  // "constants"
  BigInteger.ZERO = nbv(0);
  BigInteger.ONE = nbv(1);

/********************* jsbn.js end ************************/

/********************* prng4.js start ************************/

  // prng4.js - uses Arcfour as a PRNG

  function Arcfour() {
    this.i = 0;
    this.j = 0;
    this.S = new Array();
  }
  
  // Initialize arcfour context from key, an array of ints, each from [0..255]
  function ARC4init(key) {
    var i, j, t;
    for(i = 0; i < 256; ++i)
    this.S[i] = i;
    j = 0;
    for(i = 0; i < 256; ++i) {
    j = (j + this.S[i] + key[i % key.length]) & 255;
    t = this.S[i];
    this.S[i] = this.S[j];
    this.S[j] = t;
    }
    this.i = 0;
    this.j = 0;
  }
  
  function ARC4next() {
    var t;
    this.i = (this.i + 1) & 255;
    this.j = (this.j + this.S[this.i]) & 255;
    t = this.S[this.i];
    this.S[this.i] = this.S[this.j];
    this.S[this.j] = t;
    return this.S[(t + this.S[this.i]) & 255];
  }
  
  Arcfour.prototype.init = ARC4init;
  Arcfour.prototype.next = ARC4next;
  
  // Plug in your RNG constructor here
  function prng_newstate() {
    return new Arcfour();
  }
  
  // Pool size must be a multiple of 4 and greater than 32.
  // An array of bytes the size of the pool will be passed to init()
  var rng_psize = 256;

/********************* prng4.js end ************************/

/********************* rng.js start ************************/

  // Random number generator - requires a PRNG backend, e.g. prng4.js
  
  // For best results, put code like
  // <body onClick='rng_seed_time();' onKeyPress='rng_seed_time();'>
  // in your main HTML document.
  
  var rng_state;
  var rng_pool;
  var rng_pptr;
  
  // Mix in a 32-bit integer into the pool
  function rng_seed_int(x) {
    rng_pool[rng_pptr++] ^= x & 255;
    rng_pool[rng_pptr++] ^= (x >> 8) & 255;
    rng_pool[rng_pptr++] ^= (x >> 16) & 255;
    rng_pool[rng_pptr++] ^= (x >> 24) & 255;
    if(rng_pptr >= rng_psize) rng_pptr -= rng_psize;
  }
  
  // Mix in the current time (w/milliseconds) into the pool
  function rng_seed_time() {
    rng_seed_int(new Date().getTime());
  }
  
  // Initialize the pool with junk if needed.
  if(rng_pool == null) {
    rng_pool = new Array();
    rng_pptr = 0;
    var t;
   
    while(rng_pptr < rng_psize) {  // extract some randomness from Math.random()
    t = Math.floor(65536 * Math.random());
    rng_pool[rng_pptr++] = t >>> 8;
    rng_pool[rng_pptr++] = t & 255;
    }
    rng_pptr = 0;
    rng_seed_time();
    //rng_seed_int(window.screenX);
    //rng_seed_int(window.screenY);
  }
  
  function rng_get_byte() {
    if(rng_state == null) {
    rng_seed_time();
    rng_state = prng_newstate();
    rng_state.init(rng_pool);
    for(rng_pptr = 0; rng_pptr < rng_pool.length; ++rng_pptr)
      rng_pool[rng_pptr] = 0;
    rng_pptr = 0;
    //rng_pool = null;
    }
    // TODO: allow reseeding after first request
    return rng_state.next();
  }
  
  function rng_get_bytes(ba) {
    var i;
    for(i = 0; i < ba.length; ++i) ba[i] = rng_get_byte();
  }
  
  function SecureRandom() {}
  
  SecureRandom.prototype.nextBytes = rng_get_bytes;
  
/********************* rng.js end ************************/

/********************* rsa.js start ************************/

  // Depends on jsbn.js and rng.js
  
  // Version 1.1: support utf-8 encoding in pkcs1pad2
  
  // convert a (hex) string to a bignum object
  function parseBigInt(str,r) {
    return new BigInteger(str,r);
  }
  
  function linebrk(s,n) {
    var ret = "";
    var i = 0;
    while(i + n < s.length) {
    ret += s.substring(i,i+n) + "\n";
    i += n;
    }
    return ret + s.substring(i,s.length);
  }
  
  function byte2Hex(b) {
    if(b < 0x10)
    return "0" + b.toString(16);
    else
    return b.toString(16);
  }
  
  // PKCS#1 (type 2, random) pad input string s to n bytes, and return a bigint
  function pkcs1pad2(s,n) {
    if(n < s.length + 11) { // TODO: fix for utf-8
    alert("Message too long for RSA");
    return null;
    }
    var ba = new Array();
    var i = s.length - 1;
    while(i >= 0 && n > 0) {
    var c = s.charCodeAt(i--);
    if(c < 128) { // encode using utf-8
      ba[--n] = c;
    }
    else if((c > 127) && (c < 2048)) {
      ba[--n] = (c & 63) | 128;
      ba[--n] = (c >> 6) | 192;
    }
    else {
      ba[--n] = (c & 63) | 128;
      ba[--n] = ((c >> 6) & 63) | 128;
      ba[--n] = (c >> 12) | 224;
    }
    }
    ba[--n] = 0;
    var rng = new SecureRandom();
    var x = new Array();
    while(n > 2) { // random non-zero pad
    x[0] = 0;
    while(x[0] == 0) rng.nextBytes(x);
    ba[--n] = x[0];
    }
    ba[--n] = 2;
    ba[--n] = 0;
    return new BigInteger(ba);
  }
  
  // "empty" RSA key constructor
  function RSAKey() {
    this.n = null;
    this.e = 0;
    this.d = null;
    this.p = null;
    this.q = null;
    this.dmp1 = null;
    this.dmq1 = null;
    this.coeff = null;
  }
  
  // Set the public key fields N and e from hex strings
  function RSASetPublic(N,E) {
    if(N != null && E != null && N.length > 0 && E.length > 0) {
    this.n = parseBigInt(N,16);
    this.e = parseInt(E,16);
    }
    else
    alert("Invalid RSA public key");
  }
  
  // Perform raw public operation on "x": return x^e (mod n)
  function RSADoPublic(x) {
    return x.modPowInt(this.e, this.n);
  }
  
  // Return the PKCS#1 RSA encryption of "text" as an even-length hex string
  function RSAEncrypt(text) {
    var m = pkcs1pad2(text,(this.n.bitLength()+7)>>3);
    if(m == null) return null;
    var c = this.doPublic(m);
    if(c == null) return null;
    var h = c.toString(16);
    if((h.length & 1) == 0) return h; else return "0" + h;
  }
  
  // Return the PKCS#1 RSA encryption of "text" as a Base64-encoded string
  //function RSAEncryptB64(text) {
  //  var h = this.encrypt(text);
  //  if(h) return hex2b64(h); else return null;
  //}
  
  // protected
  RSAKey.prototype.doPublic = RSADoPublic;
  
  // public
  RSAKey.prototype.setPublic = RSASetPublic;
  RSAKey.prototype.encrypt = RSAEncrypt;
  //RSAKey.prototype.encrypt_b64 = RSAEncryptB64;
  
  //暴露RSAKey
  this.RSAKey = RSAKey;

//example:
//  var rsa = new RSAKey();
//  rsa.setPublic(encode_key, key_plus);
//  password = rsa.encrypt(password);

}).call(sinaSSOEncoder);
// function getpass(pwd,servicetime,nonce,rsaPubkey){
//  var RSAKey=new sinaSSOEncoder.RSAKey();
//  RSAKey.setPublic(rsaPubkey,'10001');
//  var password=RSAKey.encrypt([servicetime,nonce].join('\t')+'\n'+pwd);
//  return password;
// }

function GetRSA(servertime,nonce,password){
  var key="EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443";
  var RSAKey = new sinaSSOEncoder.RSAKey();
  RSAKey.setPublic(key, '10001');
  return(RSAKey.encrypt([servertime,nonce].join("\t") + "\n" + password));
}

exports.GetRSA = GetRSA;
```

baiduIndex.js

```javascript
function Dec(input, key)
{
        input   = escape(input);
        var int_key = "";
        for(var I=0;I<key.length;I++)
        {
                int_key += key.charCodeAt(I).toString();
        }

        var app = input.substr(input.length - 13,input.length);
        var app1 = app;

        app     = app ^ 99998999;

        var str = input.substr(0,input.length - 13);
        input   = str;

        int_key = int_key + app1;
        var ret = "";

        for(var I=0;I<input.length;I+=2)
        {
                var sig         = input.substr(I,2);
                sig             = parseInt(sig,16);

                var i           = (I/2) % int_key.length;
                var xor_key     = int_key.substr(i,1);
                sig             = sig ^ xor_key;

                ret             += String.fromCharCode(sig);
        }
        return unescape(ret);
}

function execEval(input, key){
  return Dec(input,key);
}
exports.execEval = execEval;
```

大家认真看的话，除了index.js文件，会发现每个文件最后都会有个exports的调用，这个按照我自己的理解是，使用exports可以使得引用他的文件直接调用里面的方法。

到这里我的web服务就基本上搭建完毕了。

在index.js文件中的

```javascript
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/weibo"] = requestHandlers.weibo;
handle["/baiduindex"] = requestHandlers.baiduindex;
```

这里其实就是给出了，url的访问地址

比如我如果要访问的话，我会这样写

[http://10.211.55.5:8006/start](http://10.211.55.5:8006/start),

[http://10.211.55.5:8006/upload](http://10.211.55.5:8006/upload),

[http://10.211.55.5:8006/weibo](http://10.211.55.5:8006/weibo),

[http://10.211.55.5:8006/baiduindex。](http://10.211.55.5:8006/baiduindex。)

后面也是可以加上参数的，然后对应的处理文件上，加上自己的处理函数，来接受不同的参数，进行自己的一些逻辑操作。

下面可以测试一下了。

在根目录下，执行

```bash
node ./index.js
```

然后再浏览器上输入url地址，就可以访问了
