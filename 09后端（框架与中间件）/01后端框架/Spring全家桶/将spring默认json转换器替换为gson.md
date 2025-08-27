# 将spring默认json转换器替换为gson

## 方式1

直接在配置文件中新增：

```properties
spring.http.converters.preferred-json-mapper=gson
spring.gson.date-format=yyyy-MM-dd HH:mm:ss
```

注：

默认的json转换器是jackson，配置一般为：

```properties
spring.jackson.date-format=yyyy-MM-dd HH:mm:ss
spring.jackson.time-zone=GMT+8
```

Spring Boot为Gson配置提供了几个属性。这是列表参考：

```properties
# 序列化日期对象时使用的格式。
spring.gson.date-format=
# 是否禁用HTML字符转义，如“<”、“>”等。
spring.gson.disable-html-escaping=
# 是否在序列化期间排除内部类。
spring.gson.disable-inner-class-serialization=
# 是否启用复杂映射键（即非原语）的序列化。
spring.gson.enable-complex-map-key-serialization=
# 是否排除所有没有“expose”注释的字段进行序列化或反序列化。
spring.gson.exclude-fields-without-expose-annotation=
# 在序列化和反序列化期间应用于对象字段的命名策略。
spring.gson.field-naming-policy=
# 是否通过在输出前添加一些特殊文本来生成不可执行的JSON。
spring.gson.generate-non-executable-json=
# 对于解析不符合RFC 4627的JSON是否宽容。
spring.gson.lenient=
# 长类型和长类型的序列化策略。
spring.gson.long-serialization-policy=
# 是否输出适合漂亮打印页面的序列化JSON。
spring.gson.pretty-printing=
# 是否序列化空字段。
spring.gson.serialize-nulls= 
```

## 方式2（推荐）

通过实现WebMvcConfigurer接口

```java
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.converter.json.GsonHttpMessageConverter;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

@Configuration
public class SpringMvcConfigure implements WebMvcConfigurer {

    /**
     * 配置消息转换器
     * @param converters
     */
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        GsonHttpMessageConverter gsonHttpMessageConverter = new GsonHttpMessageConverter();
        // 创建与配置 Gson 对象
        Gson gson = new GsonBuilder()
                .setDateFormat("yyyy-MM-dd HH:mm:ss")
                .excludeFieldsWithoutExposeAnnotation()
                .disableHtmlEscaping()
                .create();
        gsonHttpMessageConverter.setGson(gson);
        // 将其放在首位
        converters.add(0, gsonHttpMessageConverter);
    }

}
```

注：

1. 可以自定义一些Gson属性
2. 除了configureMessageConverters方法，也可以覆盖extendMessageConverters方法
3. 如果工程中extends WebMvcConfigurationSupport，可能会覆盖掉WebMvcConfigurer中的方法，可以通过断点调试是否进入

> 也就是说我们为添加跨域支持时继承了WebMvcConfigurationSupport，（可以使用webmvcconfigureAdapter ，但是因为我使用的是SpringBoot2.x
> 以上的版本，该抽象类已经被废弃）而在WebMvc 自动装配的配置类中，指定了WebMvc的加载条件
>
> + 当环境中（IOC容器）存在Servlet、 DispatcherServlet、 WebMvcConfigurer 时加载WebMvc配置
> + 当环境中存在WebMvcConfigurationSupport Bean时不加载此配置，也就是说不能有WebMvcConfigurationSupport
>
> 所以这也就解释了我们新添加的拦截器不生效的原因了！

## 方式3

1、pom依赖

```xml

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <!-- 去除默认的jackson -->
    <exclusions>
        <exclusion>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </exclusion>
    </exclusions>
</dependency>
        <!-- Gson -->
<dependency>
<groupId>com.google.code.gson</groupId>
<artifactId>gson</artifactId>
</dependency>
```

2、配置文件
在写配置文件前，先对之前的Student类进行修改，去除所有属性上的注解，并将Sex属性修改为protected，这是因为Gson可以指定被某类修饰符所修饰的属性进行忽略。
SpringBoot使用Gson可以像jackson一样，因为提供了自动转换类。但是想要对日期进行格式化，需要自己提供自定义的HttpMessagerConverter。

```java

@Configuration
public class GsonConfig {
    @Bean
    public GsonHttpMessageConverter gsonHttpMessageConverter() {
        GsonHttpMessageConverter converter = new GsonHttpMessageConverter();
        GsonBuilder builder = new GsonBuilder();
        // 设置解析日期的格式
        builder.setDateFormat("yyyy-MM-dd HH:MM:SS");
        // 过滤修饰符为protected的属性
        builder.excludeFieldsWithModifiers(Modifier.PROTECTED);
        Gson gson = builder.create();
        converter.setGson(gson);
        return converter;
    }
}
```

参考：

[1] spring boot 2.x 添加拦截器配置未生效的问题 https://www.jianshu.com/p/b6c510fb10f5

[2] 记一次踩坑:springboot2.0.2配置fastjson不生效 https://segmentfault.com/a/1190000015975405

[3] SpringBoot - Jackson、Gson、fastJson返回JSON数据 https://www.codeleading.com/article/88623202968/

[4] 浅析Gson与Spring Boot https://its401.com/article/weixin_34266504/91478813
