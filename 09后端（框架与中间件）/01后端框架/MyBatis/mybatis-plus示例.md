# mybatis-plus示例


### application.yml

```yml
spring:
    #数据库配置
    datasource:
        driver-class-name: org.sqlite.JDBC
        url: jdbc:sqlite:/Users/givedrug/onedrive/data/testreport.db
        username: ''
        password: ''
```

### pom.xml

```xml
<!--lombok：自动bean插件-->
<dependency>
	<groupId>org.projectlombok</groupId>
	<artifactId>lombok</artifactId>
	<version>1.18.10</version>
	<scope>provided</scope>
</dependency>

<!--mybatis plus-->
<dependency>
	<groupId>com.baomidou</groupId>
	<artifactId>mybatis-plus-boot-starter</artifactId>
	<version>3.2.0</version>
</dependency>

<!--sqlite jdbc-->
<dependency>
	<groupId>org.xerial</groupId>
	<artifactId>sqlite-jdbc</artifactId>
	<version>3.28.0</version>
</dependency>
```

### xxxApplication.java

```java
@SpringBootApplication
@MapperScan("com.test.testreportback.mapper")
public class TestReportBackApplication {

	public static void main(String[] args) {
		SpringApplication.run(TestReportBackApplication.class, args);
	}

}
```

### xxxController.java

```java
@Controller
public class projectController {

    @Autowired
    private projectService projectservice;

    @PostMapping("/project")
    @ResponseBody
    public boolean insertProject(projectModel projectParam){
        System.out.println(projectParam);

        projectParam.setCreatetime(new Date().toString());
        projectParam.setModifytime(new Date().toString());
        return projectservice.insertProject(projectParam);
    }

    @GetMapping("/project")
    @ResponseBody
    public projectModel getProject(String projectid){
        return projectservice.getProject(projectid);
    }

    @PutMapping("/project")
    @ResponseBody
    public boolean updateProject(projectModel projectParam){

        return projectservice.updateProject(projectParam);
    }

    @DeleteMapping("/project")
    @ResponseBody
    public boolean deleteProject(String projectid){
        return projectservice.deleteProject(projectid);
    }

    @GetMapping("/allproject")
    @ResponseBody
    public List<projectModel> getAllProject(){
        return projectservice.getAllProject();
    }

}
```

### xxxMaper.java

```java
@Mapper
public interface projectMapper extends BaseMapper<projectModel>{

}
```

### xxxModel.java

```java
@Data
@TableName(value = "project")
public class projectModel {
    @TableId
    private String projectid;

    private String productname;
    private String projectname;
    private Integer status;
    private String tester;
    private String createtime;
    private String modifytime;
}
```

### xxxService.java

```java
public interface projectService extends IService<projectModel>{

    //插入新project
    boolean insertProject(projectModel projectmodel);

    //根据projectid获取记录
    projectModel getProject(String projectid);

    //更新project
    boolean updateProject(projectModel projectmodel);

    //删除project
    boolean deleteProject(String projectid);

    //获取所有project
    List<projectModel> getAllProject();

}
```

### xxxServiceImpl.java

```java
@Service
public class projectServiceImpl extends ServiceImpl<projectMapper,projectModel> implements projectService {

    @Override
    public boolean insertProject(projectModel projectmodel) {
        return save(projectmodel);
    }

    @Override
    public projectModel getProject(String projectid){
        return getById(projectid);
    }

    @Override
    public boolean updateProject(projectModel projectmodel) {
        return updateById(projectmodel);
    }

    @Override
    public boolean deleteProject(String projectid) {
        return removeById(projectid);
    }

    @Override
    public List<projectModel> getAllProject() {
        return list();
    }

}
```
