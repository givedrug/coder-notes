# clearfix清除浮动


在网页布局中，当子元素使用了浮动（float）后，可能会导致父容器出现“高度塌陷”的问题。简单来说，父容器无法根据浮动子元素的高度自动撑开，导致布局错乱。为了解决这个问题，可以使用一个常见的CSS技巧——“clearfix”。

“清除浮动”的核心思想是：通过在父容器的末尾创建一个“伪元素”，并设置其 clear 属性来阻止浮动元素影响父容器的高度计算。

```css
/*
* For modern browsers
* 1. The space content is one way to avoid an Opera bug when the
*  contenteditable attribute is included anywhere else in the document.
*  Otherwise it causes space to appear at the top and bottom of elements
*  that are clearfixed.
* 2. The use of `table` rather than `block` is only necessary if using
* `:before` to contain the top-margins of child elements.
*/
.clearfix:before,
.clearfix:after {
 content: " "; /* 1 */
 display: table; /* 2 */
}

.clearfix:after {
 clear: both;
}

/*
* For IE 6/7 only
* Include this rule to trigger hasLayout and contain floats.
*/
.clearfix {
 zoom: 1;
}
```
