# （问题）data是否使用return的区别是什么？


```javascript
// Vue实例中data属性是如下方式展示的：
let app = newVue({

    el: "#app",
    data: { msg: '' },
    methods: {}
})

// 使用组件化的项目中是如下方式展示的:
export default{
    data(){
        return{
            showLogin:true,
            msg:''
        }
    },
    methods:{}
}

// 为何在大型项目中data需要使用return返回数据呢？
// 答：不使用return包裹的数据会在项目的全局可见，会造成变量污染
// 使用return包裹后数据中变量只在当前组件中生效，不会影响其他组件
```
