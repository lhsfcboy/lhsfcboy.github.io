和一般文章不同，本文不依赖于任何现有的框架，也不试图陷入冗长的发展历史，而是完全从头开始，以一个尽可能小但是可以说明问题的案例，以此讲清楚MVC这个历史悠久、变型极多的技术理念。MVC是一种非常普及的，基础的设计套路，在不同的语言社区内都有着大量的应用。理解了MVC，学习接下来的MVVM、MVP等才能成为可能。
MVC把一个系统的类分为三种：Model，View和Controller。它们也遵循着职责分离原则：
	1. 由Controller来处理消息
	2. 由Model掌管数据源
	3. 由View负责数据显示
尽管MVC看起来复杂，其实用代码表达最简单的MVC是可能的：
/** 模拟 Model, View, Controller */
var M = {}, V = {}, C = {};

/** Model 负责数据 */
M.data = "hello world";
/** View 负责输出 */
V.render = (M) => { alert(M.data); }
/** Controller 搭桥*/
C.handleOnload = () => { V.render(M); }
window.onload = C.handleOnload;

只要是和用户交互的都是View，所以使用alert，或者直接输出到console，都是一种View。
接下来，我希望用一个完整但是极简的程序，来验证MVC如何从一个日常的程序进化而来的。这个一个小型程序只不过是如此：
1 + - 
点击按钮会让span加1或者减1。它简单到你不需要分心关注，但是由足够说明典型的html场景——就是既有数据呈现也有按钮操作。 
<div id="app">
<p><span id="count">0</span>
    <button id="inc">+</button>
    <button id="dec">-</button>
  </p>
</div>
<script>
    var counter = document.getElementById('count');
    var btn1 = document.getElementById('inc');
    var btn2 = document.getElementById('dec');
    var count = 0;
    btn1.addEventListener('click',function (){
                counter.innerHTML = ++count;
            }
    )
    btn2.addEventListener('click',function (){
                counter.innerHTML = --count;
            }
    )
</script>
当前的小型程序，所有的代码，无论数据还是逻辑还是UI代码，都是混合在一起的，并没有所谓的任何的职责分离。因为还小，问题不大。但是产品代码都是从这一的基础上逐步长大的。比如说数据就不太可能只有一个count，代码逐步增大，一个对象的数据属性会越来越多，随着来的是操作数据的函数也会越来越多。同理包括用户界面和业务逻辑。
如果使用MVC的眼光来看，在此微观模式下，其实可以使用MVC的模式做代码的职责分离。其中所有的UI元素对象，都应该放置到View类型内，其中的事件处理都是应该放到Controller内，而数据，也就是这里的count变量和对它的操作（减一加一），应该放置到Model类内，组装Model和View则是Controller的职责。这样的思路下，代码可以改成：
<div id="app">
<p><span id="count">1</span>
    <button id="inc">+</button>
    <button id="dec">-</button>
  </p>
</div>
<script>
    class Model{
      constructor(){
        this.count = 1
      }
      inc(){
        return this.count++
      }
      dec(){
        return this.count--
      }
    }
    class View{
      constructor(){
        this.counter = document.getElementById('count')
        this.btn1 = document.getElementById('inc')
        this.btn2 = document.getElementById('dec')
      }
      setCount(c){
       this.counter.innerHTML = c 
      }
      attachInc(cb){
        this.btn1.addEventListener('click',cb)
      }
      attachDec(cb){
        this.btn2.addEventListener('click',cb)
      }
    }
    class Controller {
      constructor(){
        this.m = new Model()
        this.v = new View()
        this.v.attachInc(this.onInc.bind(this))
        this.v.attachDec(this.onDec.bind(this))
      }
      onInc(){
        this.v.setCount(this.m.inc())
      }
      onDec(){
        this.v.setCount(this.m.dec())
      }
    }
    var c = new Controller()
</script>
将应用程序划分为三种组件，模型 - 视图 - 控制器（MVC）设计定义它们之间的相互作用。
Model用于封装数据以及对数据的处理方法。Model不依赖“View”和“Controller”，也就是说， Model 不关心它会被如何显示或是如何被操作。Model 中数据的变化一般会通过一种刷新机制被公布。为此，Model需要提供被监听的机制。
View能够实现显示。在 View 中一般没有程序上的逻辑。为了实现Model变化后的响应View 上的刷新功能，View需要监听Model的变化。
控制器（Controller）起到不同层面间的组织作用，用于控制应用程序的流程。它处理事件并作出响应。“事件”包括用户的行为和数据 Model 上的改变。


实际上，通过观察者模式，可以把Model的修改刷新到多个视图中，只要视图做一个Model变化的订阅即可。可以先做一个简单的观察者代码：
var Event = function (sender) {
    this._sender = sender;
    this._listeners = [];
}
Event.prototype = {
    attach: function (listener) {
        this._listeners.push(listener);
    },
    notify: function (args) {
        for (var i = 0; i < this._listeners.length; i += 1) {
            this._listeners[i](this._sender, args);
        }
    }
};
然后把应用稍作修改，在加上一个span，其中为第一个span的值乘以2。界面看起来是这样：
1|2 + - 
这就意味着，一个count的模型值，先做有两个span需要消费它，因此无论何种原因导致count的修改，两个span都应该同步的被修改。此时我们可以利用Event对象，让View订阅count修改的时间，当count修改时，就会通知视图，做相应的修改。完整的代码如下： 
<div id="app">
<p><span id="count">1</span>|<span id="count2">2</span>
    <button id="inc">+</button>
    <button id="dec">-</button>
  </p>
</div>
<script>
    class Model{
      constructor(e){
        this.e = e
        this.count = 1
      }
      inc(){
        this.count++
        this.e.notify(this.count)
        return this.count
      }
      dec(){
        this.count--
        this.e.notify(this.count)
        return this.count
      }
    }
    class View{
      constructor(e){
        this.e = e
        this.e.attach(this.f.bind(this))
        this.counter = document.getElementById('count')
        this.counter2 = document.getElementById('count2')
        this.btn1 = document.getElementById('inc')
        this.btn2 = document.getElementById('dec')
      }
      f(sender,c){
        this.counter2.innerHTML = c * 2
      }
      setCount(c){
       this.counter.innerHTML = c 
      }
      attachInc(cb){
        this.btn1.addEventListener('click',cb)
      }
      attachDec(cb){
        this.btn2.addEventListener('click',cb)
      }
    }
    var Event = function (sender) {
        this._sender = sender;
        this._listeners = [];
    }
    Event.prototype = {
        attach: function (listener) {
            this._listeners.push(listener);
        },
        notify: function (args) {
            for (var i = 0; i < this._listeners.length; i += 1) {
                this._listeners[i](this._sender, args);
            }
        }
    };
    class Controller {
      constructor(){
        this.e = new Event()
        this.m = new Model(this.e)
        this.v = new View(this.e)
        this.v.attachInc(this.onInc.bind(this))
        this.v.attachDec(this.onDec.bind(this))
      }
      onInc(){
        this.v.setCount(this.m.inc())
      }
      onDec(){
        this.v.setCount(this.m.dec())
      }
    }
    var c = new Controller()
</script>
此应用的最后一个实现，看起来更加具备了一个MVC的多个方面：
	1. 类职责分类为模型视图控制器
	2. 有了事件的发布和订阅的机制，可以更好的发布一个模型的变化到多个视图去
	3. Model并不依赖于View，而是通过事件发布订阅的方式通知视图变化


作者：刘传君
链接：https://juejin.im/post/5a55b1246fb9a01cb31610e6
来源：掘金
