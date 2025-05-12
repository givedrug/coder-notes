# Base64编码


Base64 就是一种编码方法，可以将任意值转成 0～9、A～Z、a-z、+ 和 / 这 64 个字符组成的可打印字符

要将非 ASCII 码字符转为 Base64 编码，必须中间插入一个转码（转为 URL 编码）环节，再使用这两个方法，对应的 JavaScript 代码为：

```javascript
function b64Encode(str) {
  return btoa(encodeURIComponent(str));
}
 
function b64Decode(str) {
  return decodeURIComponent(atob(str));
}

// btoa()：任意值转为 Base64 编码
// atob()：Base64 编码转为原来的值
b64Encode('你好')// "JUU0JUJEJUEwJUU1JUE1JUJE"
b64Decode('JUU0JUJEJUEwJUU1JUE1JUJE')// "你好"
```

在 Java 中，要达到与 JavaScript btoa(encodeURIComponent()) 和 decodeURIComponent(atob()) 相同的效果，核心思路也一样：先进行 URL 编码，再进行 Base64 编码，反之亦然。

下面给出一个示例，使用 Java 8+ 自带的 Base64（位于 java.util 包）以及 URLEncoder / URLDecoder 来实现：

```java
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class Base64Util {

    /**
     * 先将字符串 URL 编码，然后再进行 Base64 编码。
     * @param str 待编码的字符串
     * @return 编码后的字符串
     */
    public static String b64Encode(String str) {
        try {
            // 1. URL 编码（encodeURIComponent 等效）
            String urlEncoded = URLEncoder.encode(str, StandardCharsets.UTF_8.toString());
            // 2. 使用 Java 内置的 Base64 进行编码
            return Base64.getEncoder().encodeToString(urlEncoded.getBytes(StandardCharsets.UTF_8));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 先对 Base64 解码，然后再进行 URL 解码，还原原始字符串。
     * @param base64Str 已经 Base64 编码的字符串
     * @return 解码后的原始字符串
     */
    public static String b64Decode(String base64Str) {
        try {
            // 1. Base64 解码
            byte[] decodedBytes = Base64.getDecoder().decode(base64Str);
            // 2. URL 解码（decodeURIComponent 等效）
            return URLDecoder.decode(new String(decodedBytes, StandardCharsets.UTF_8), StandardCharsets.UTF_8.toString());
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String[] args) {
        // 测试
        String originalStr = "你好";
        String encoded = b64Encode(originalStr);
        String decoded = b64Decode(encoded);

        System.out.println("原文: " + originalStr);
        System.out.println("编码后: " + encoded);   // 对应 JS: "JUU0JUJEJUEwJUU1JUE1JUJE"
        System.out.println("解码后: " + decoded);   // "你好"
    }
}
```

注意，对于 URL 或者 MIME 场景下，java 包提供了专门的方法来处理：

```java
// URL安全的编码和解码 (用于 URL 安全的 Base64 编码和解码，会将 `+` 和 `/` 分别替换为 `-` 和 `_`，并且不添加填充字符 `=`)
String urlEncodedString = Base64.getUrlEncoder().encodeToString(originalString.getBytes());
System.out.println("URL Encoded String: " + urlEncodedString);

byte[] urlDecodedBytes = Base64.getUrlDecoder().decode(urlEncodedString);
String urlDecodedString = new String(urlDecodedBytes);
System.out.println("URL Decoded String: " + urlDecodedString);


// MIME 编码 (适用于邮件等场景, 每行最多76个字符，并以\r\n结尾)
String mimeEncodedString = Base64.getMimeEncoder().encodeToString(originalString.getBytes());
System.out.println("MIME Encoded String: " + mimeEncodedString);

byte[] mimeDecodedBytes = Base64.getMimeDecoder().decode(mimeEncodedString);
String mimeDecodedString = new String(mimeDecodedBytes);
System.out.println("MIME Decoded String: " + mimeDecodedString);
```
