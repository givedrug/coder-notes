# RESTful API与mybatis注解方式完整示例

## 目录结构

```
├── pom.xml
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │   └── example
│   │   │   └── mybatisdemo
│   │   │   ├── MybatisDemoApplication.java
│   │   │   ├── controller
│   │   │   │   └── TaskController.java
│   │   │   ├── mapper
│   │   │   │   └── TaskMapper.java
│   │   │   ├── model
│   │   │   │   └── TaskModel.java
│   │   │   └── service
│   │   │   ├── TaskService.java
│   │   │   └── impl
│   │   │   └── TaskServiceImpl.java
│   │   └── resources
│   │   └── application.properties
```

## RESTful API 调用

增：

```
curl --location --request POST '127.0.0.1:8080/demo/task' \
--header 'Content-Type: application/json' \
--data-raw '{
    "taskType":"red",
    "taskName":"redtask1"
}'
```

查：

```
curl --location --request GET '127.0.0.1:8080/demo/task?taskId=1'
```

改：

```
curl --location --request PUT '127.0.0.1:8080/demo/task' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id":1,
    "taskType":"red",
    "taskName":"redtaskupdate"
}'
```

删：

```
curl --location --request DELETE '127.0.0.1:8080/demo/task?taskId=1'
```

查全部：

```
curl --location --request GET '127.0.0.1:8080/demo/all'
```

## 代码

### demo_task.sql

```sql
CREATE TABLE demo_task
(
    `id`        bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
    `task_type` varchar(45) NOT NULL DEFAULT '' COMMENT '任务类型：split拆分任务，merge聚合任务',
    `task_name` varchar(45) NOT NULL DEFAULT '' COMMENT '任务类型：split拆分任务，merge聚合任务',
    create_time timestamp            default CURRENT_TIMESTAMP not null comment '创建时间',
    update_time timestamp            default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间',
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```

### pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.6</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>mybatis-demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>mybatis-demo</name>
    <description>mybatis-demo</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>1.3.2</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>

```

### application.properties

```properties
spring.application.name=mybatisdemo
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/gist_demo?useUnicode=true&characterEncoding=utf-8&autoReconnect=true&serverTimezone=Asia/Shanghai&zeroDateTimeBehavior=convertToNull&useAffectedRows=true
spring.datasource.username=root
spring.datasource.password=123456
mybatis.configuration.mapUnderscoreToCamelCase=true
```

### TaskController.java

```java
package com.example.mybatisdemo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.mybatisdemo.model.TaskModel;
import com.example.mybatisdemo.service.TaskService;

@RestController
@RequestMapping(value = "/demo")
public class TaskController {

    @Autowired
    private TaskService taskService;

    @PostMapping("/task")
    @ResponseBody
    public int insertTask(@RequestBody TaskModel taskModel) {
        return taskService.insertTask(taskModel);
    }

    @GetMapping("/task")
    @ResponseBody
    public TaskModel getTask(long taskId) {
        return taskService.getTaskById(taskId);
    }

    @PutMapping("/task")
    @ResponseBody
    public int updateTask(@RequestBody TaskModel taskModel) {
        return taskService.updateTask(taskModel);
    }

    @DeleteMapping("/task")
    @ResponseBody
    public int deleteTask(long taskId) {
        return taskService.deleteTask(taskId);
    }

    @GetMapping("/all")
    @ResponseBody
    public List<TaskModel> getAllTasks() {
        return taskService.getAllTasks();
    }

}

```

### TaskService.java

```java
package com.example.mybatisdemo.service;

import java.util.List;

import com.example.mybatisdemo.model.TaskModel;

public interface TaskService {
    /**
     * 插入task
     * @param taskModel
     * @return
     */
    int insertTask(TaskModel taskModel);

    /**
     * 通过id获取task
     * @param taskId
     * @return
     */
    TaskModel getTaskById(long taskId);

    /**
     * 更新task
     * @param taskModel
     * @return
     */
    int updateTask(TaskModel taskModel);

    /**
     * 通过id删除task
     * @param taskId
     * @return
     */
    int deleteTask(long taskId);

    /**
     * 获取所有task
     * @return
     */
    List<TaskModel> getAllTasks();
}

```

### TaskServiceImpl.java

```java
package com.example.mybatisdemo.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.mybatisdemo.mapper.TaskMapper;
import com.example.mybatisdemo.model.TaskModel;
import com.example.mybatisdemo.service.TaskService;

@Service
public class TaskServiceImpl implements TaskService {

    @Autowired
    private TaskMapper taskMapper;

    @Override
    public int insertTask(TaskModel taskModel) {
        return taskMapper.insertTask(taskModel);
    }

    @Override
    public TaskModel getTaskById(long taskId) {
        return taskMapper.getTaskById(taskId);
    }

    @Override
    public int updateTask(TaskModel taskModel) {
        return taskMapper.updateTask(taskModel);
    }

    @Override
    public int deleteTask(long taskId) {
        return taskMapper.deleteTask(taskId);
    }

    @Override
    public List<TaskModel> getAllTasks() {
        return taskMapper.getAllTasks();
    }
}

```

### TaskModel.java

```java
package com.example.mybatisdemo.model;

import java.util.Date;

import lombok.Data;

@Data
public class TaskModel {
    /**
     * 自增主键
     */
    private long id;

    /**
     * task类型
     */
    private String taskType;

    /**
     * task名称
     */
    private String taskName;

    /**
     * 创建时间
     */
    private Date createTime;

    /**
     * 更新时间
     */
    private Date updateTime;

}

```

### TaskMapper.java

```java
package com.example.mybatisdemo.mapper;

import java.util.List;

import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import com.example.mybatisdemo.model.TaskModel;

@Mapper
@Repository
public interface TaskMapper {
    @Insert("INSERT INTO demo_task (task_type, task_name) VALUES (#{taskType}, #{taskName})")
    int insertTask(TaskModel taskModel);

    @Select("SELECT * FROM demo_task WHERE id = #{taskId}")
    TaskModel getTaskById(long taskId);

    @Update("UPDATE demo_task SET task_type=#{taskType}, task_name=#{taskName} WHERE id = #{id}")
    int updateTask(TaskModel taskModel);

    @Delete("DELETE FROM demo_task WHERE id = #{taskId}")
    int deleteTask(long taskId);

    @Select("SELECT * FROM demo_task")
    List<TaskModel> getAllTasks();
}

```
