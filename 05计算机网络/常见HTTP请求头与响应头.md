# 常见HTTP请求头与响应头


### HTTP 请求头

- `User-Agent`：产生请求的浏览器类型。
- `Accept`：客户端可识别的响应内容类型列表。
- `Accept-Language`：客户端可接受的自然语言。
- `Accept-Encoding`：客户端可接受的编码压缩格式。
- `Accept-Charset`：可接受的应答的字符集。
- `Host`：请求的主机名，允许多个域名同处一个IP 地址，即虚拟主机。（必选）
- `Connection`：连接方式(close 或 keep-alive)。
- `Cookie`：存储于客户端扩展字段，向同一域名的服务端发送属于该域的cookie。
- `Referer`：包含一个URL，用户从该URL代表的页面出发访问当前请求的页面。
- `If-Modified-Since`：文档的最后改动时间。

### HTTP 响应头

- `Allow`：服务器支持哪些请求方法（如GET、POST等）。
- `Content-Encoding`：文档的编码（Encode）方法。
- `Content-Length`：表示内容长度。只有当浏览器使用持久HTTP连接时才需要这个数据。
- `Content-Type`：表示后面的文档属于什么MIME类型。
- `Date`：当前的GMT时间。你可以用setDateHeader来设置这个头以避免转换时间格式的麻烦。
- `Expires`：应该在什么时候认为文档已经过期，从而不再缓存它。
- `Last-Modified`：文档的最后改动时间。
- `Refresh`：表示浏览器应该在多少时间之后刷新文档，以秒计。
- `Server`：服务器名字。
- `Set-Cookie`：设置和页面关联的Cookie。
- `ETag`：被请求变量的实体值。ETag是一个可以与Web资源关联的记号（MD5值）。
- `Cache-Control`：这个字段用于指定所有缓存机制在整个请求/响应链中必须服从的指令。
