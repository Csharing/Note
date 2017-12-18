//这是注释
/*这是注释*/
/*
数据类型：
Number类型123;0.123;1.23e3;-99;NaN;Infinity无限大
字符串：'';""
布尔型：True;False;与操作:&&;或操作:||;非操作:!
比较运算符：>;<;===优于==;
NaN==NaN为False,只能通过isNaN()判断
判断浮点数，只能判断它们的精度
Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; 
null相当于python中的None
数组：[1, 2, 3.14, 'Hello', null, true]存储任意类型的值，通过索引访问
对象：var xiaohong = {name: '小红','school': 'Middle'};是一组由键-值组成的无序集合，相当于python的字典，通过键获取，键必须为字符串
Map：var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);m.get('Michael'); //对象的优化，键的值无要求
set： var s = new Set([1, 2, 3, 3, '3']);相当于queue有add，delete方法
申明变量用var，var $b = 1,a=1；
iterable类型：
Array、Map和Set都属于iterable类型。
遍历：
	for of：
		var a = ['A', 'B', 'C'];
		var s = new Set(['A', 'B', 'C']);
		var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
		for (var x of a) { // 遍历Array
			console.log(x);
		}
		for (var x of s) { // 遍历Set
			console.log(x);
		}
		for (var x of m) { // 遍历Map
			console.log(x[0] + '=' + x[1]);
		}
	forEach：
		'use strict';
		var a = ['A', 'B', 'C'];
		a.forEach(function (element, index, array) {
		// element: 指向当前元素的值
		// index: 指向当前索引
		// array: 指向Array对象本身
		console.log(element + ', index = ' + index);
		});
		值，索引，self若没有则向后填充

函数：
定义函数：
	function abs(x) {
    if (typeof x !== 'number') {
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
函数允许多传入参数，多余的会忽略，arguments可以获取所有的值，...rest写在参数的最后面用于获取多余的值
可以在定义函数的时候再定义一个值
window为最高层次的全局变量
用let替换var可以使i	仅作用于for循环内部，const声明一个常量不可修改
ES6开始的解构赋值方式：var [x, y, z] = ['hello', 'JavaScript', 'ES6'];如果有嵌套只需要保持结构一致即可
var {name, age, passport} = person;利用键来获取值，如果有嵌套只需要保持结构一致即可
如果已经赋值了，({x, y} = { name: '小明', x: 100, y: 200});则需要使用小括号包起来，防止判定为块
方法：
	this同于self，调用函数使用new，this的作用只对当前块有用
	var xiaoming = {
		name: '小明',
		birth: 1990,
		age: function () {
			var y = new Date().getFullYear();
			return y - this.birth;
		}
	};
	
生成器：
function* foo(x) {
    yield x + 1;
    yield x + 2;
    return x + 3;
}
constructor：构造函数
	
extends：继承于
class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name); // 记得用super调用父类的构造方法!
        this.grade = grade;
    }

    myGrade() {
        alert('I am at grade ' + this.grade);
    }
}	

var width = window.innerWidth || document.body.clientWidth;
要加载一个新页面，可以调用location.assign()。如果要重新加载当前页面，调用location.reload()方法非常方便。
用document对象提供的getElementById()和getElementsByTagName()可以按ID获得一个DOM节点和按Tag名称获得一组DOM节点：
JavaScript可以通过document.cookie读取到当前页面的Cookie：
为了解决这个问题，服务器在设置Cookie时可以使用httpOnly，设定了httpOnly的Cookie将不能被JavaScript读取。这个行为由浏览器实现，主流浏览器均支持httpOnly选项，IE从IE6 SP1开始支持。
这个对象属于历史遗留对象，对于现代Web页面来说，由于大量使用AJAX和页面交互，简单粗暴地调用history.back()可能会让用户感到非常愤怒。



始终记住DOM是一个树形结构。操作一个DOM节点实际上就是这么几个操作：

更新：更新该DOM节点的内容，相当于更新了该DOM节点表示的HTML的内容；

遍历：遍历该DOM节点下的子节点，以便进行进一步操作；

添加：在该DOM节点下新增一个子节点，相当于动态增加了一个HTML节点；

删除：将该节点从HTML中删除，相当于删掉了该DOM节点的内容以及它包含的所有子节点。

查：
由于ID在HTML文档中是唯一的，所以document.getElementById()可以直接定位唯一的一个DOM节点。document.getElementsByTagName()和document.getElementsByClassName()总是返回一组DOM节点。要精确地选择DOM，可以先定位父节点，再从父节点开始选择，以缩小范围
var reds = document.getElementById('test-div').getElementsByClassName('red');

改：
一种是修改innerHTML属性，这个方式非常强大，不但可以修改一个DOM节点的文本内容，还可以直接通过HTML片段修改DOM节点内部的子树：
p.innerHTML = 'ABC <span style="color:red">RED</span> XYZ';

第二种是修改innerText或textContent属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签：
两者的区别在于读取属性时，innerText不返回隐藏元素的文本，而textContent返回所有文本。另外注意IE<9不支持textContent。
要删除一个节点，首先要获得该节点本身以及它的父节点，然后，调用父节点的removeChild把自己删掉：


表单：
HTML表单的输入控件主要有以下几种：

文本框，对应的<input type="text">，用于输入文本；

口令框，对应的<input type="password">，用于输入口令；

单选框，对应的<input type="radio">，用于选择一项；

复选框，对应的<input type="checkbox">，用于选择多项；

下拉框，对应的<select>，用于选择一项；

隐藏文本，对应的<input type="hidden">，用户不可见，但表单提交时会把隐藏文本发送到服务器。

注意到id为md5-password的<input>标记了name="password"，而用户输入的id为input-password的<input>没有name属性。没有name属性的<input>的数据不会被提交。


Promise
异步调用


jQuery这么流行，肯定是因为它解决了一些很重要的问题。实际上，jQuery能帮我们干这些事情：

消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；

简洁的操作DOM的方法：写$('#test')肯定比document.getElementById('test')来得简洁；

轻松实现动画、修改CSS等各种操作。


var div = $('#abc');














	
注意：JavaScript引擎会在行末自动添加分号，以{结尾则不加，需要注意{}的使用



strict模式
*/
'use strict';
var x=100;
console.log(x);