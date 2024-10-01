剪辑自: https://mp.weixin.qq.com/s/63CD7d2uE-OZKooZU3RN5Q

本文重点是封装一个高级MVP架构，会详细的讲解如何一步步从无到有的封装成一个高级MVP架构过程。 

众所周知普通的MVP模式可能存在内存泄露、代码冗余、界面意外关闭后在重建数据缓存等问题，本文最终封装的成果为一一解决这些问题，而且在使用过程中尽量做到使用简单而且可扩展,当然本文也只是提供了一种封装思路而已，如果不能满足你的需求还可以自行再进行扩展。


如果你觉得你不想看整个实现思路可以直接看最后的源码，望给点个star鼓励一下
GitHub地址：
https://github.com/ljqloveyou123


文章会以5个部分来整体优化封装MVP，也是一个从无到有的过程


	• 一、不使用MVP的代码
	• 二、最简单的MVP实现
	• 三、解决MVP内存泄露
	• 四、简单抽象-解决MVP代码冗余
	• 五、高级抽象-使用注解、工厂模式、代理模式、策略模式整体解决代码冗余、内存泄露、Presenter生命周期以及数据存储问题


不废话了，进入正题。


场景：假如界面有一个按钮，点击后请求数据，然后成功后将返回的数据设置到一个Textview中




一、不使用MVP的代码,一般我们会这么写 



public class MainActivity extends AppCompatActivity {
    @FieldView(R.id.tv_text)
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ViewFind.bind(this);
    }
    //按钮点击事件
    public void request(View view) {
        clickRequest("101010100");
    }
    //发起请求
    public void clickRequest(final String cityId) {
        //请求接口
        Retrofit retrofit = new Retrofit.Builder()
                //代表root地址
                .baseUrl("http://www.weather.com.cn/")
                .addConverterFactory(ScalarsConverterFactory.create())
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        ApiService apiService = retrofit.create(ApiService.class);
        //请求
        Call<WeatherBean> weatherBeanCall = apiService.requestWeather(cityId);
        weatherBeanCall.enqueue(new Callback<WeatherBean>() {
            @Override
            public void onResponse(Call<WeatherBean> call, Response<WeatherBean> response) {
                //请求成功
                textView.setText(response.body().getWeatherinfo().toString());
            }
            @Override
            public void onFailure(Call<WeatherBean> call, Throwable t) {
                //请求失败
            }
        });
    }
}



上面的代码是最原始的写法，下面我们使用最简单的MVP模式来改造这个代码。




思路如下： 


1、首先我们先定义一个接口，用来规定针对这个界面逻辑View需要作出的动作的接口。 
2、让Activity实现这个接口中的方法，也就是V层 
3、创建一个类，用来封装之前的网络请求过程，也就是M层 
4、再创建一个类，用来处理M层和V层之间的通信，也就是P层


下面来实现一下：


1、首先我们先定义一个接口，用来规定针对这个界面逻辑View需要作出的动作的接口。


/**
 * @author 刘镓旗
 * @date 2017/11/16
 * @description V层接口，定义V层需要作出的动作的接口
 */
public interface RequestView1 {
    //请求时展示加载
    void requestLoading();
    //请求成功
    void resultSuccess(WeatherBean result);
    //请求失败
    void resultFailure(String result);
}



2、让Activity实现这个接口中的方法，也就是V层 



/**
 *   第二步：对应demo1
 * 2，最简单的mvp模式,
 * 1.Activity需要实现v层接口
 * 2.Persenter需要持有v层引用和m层引用
 * 3.在实现类view中创建persenter
 */
public class MainActivity extends AppCompatActivity implements RequestView1 {
    @FieldView(R.id.tv_text)
    private TextView textView;
    private RequestPresenter1 presenter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ViewFind.bind(this);
        //创建Presenter
        presenter = new RequestPresenter1(this);
    }
    //点击事件
    public void request(View view) {
        presenter.clickRequest("101010100");
    }
    //请求时加载
    @Override
    public void requestLoading() {
        textView.setText("请求中,请稍后...");
    }
    //请求成功
    @Override
    public void resultSuccess(WeatherBean result) {
        //成功
        textView.setText(result.getWeatherinfo().toString());
    }
    //请求失败
    @Override
    public void resultFailure(String result) {
        //失败
        textView.setText(result);
    }
}



3、创建一个类，用来封装之前的网络请求过程，也就是M层 



/**
 * @description M层 数据层
 */
public class RequestMode1 {
    private static final String BASE_URL = "http://www.weather.com.cn/";
    //http://www.weather.com.cn/data/cityinfo/101010100.html
   public void request(String detailId, Callback<WeatherBean> callback){
       //请求接口
       Retrofit retrofit  = new Retrofit.Builder()
               //代表root地址
               .baseUrl(BASE_URL)
               .addConverterFactory(ScalarsConverterFactory.create())
               .addConverterFactory(GsonConverterFactory.create())
               .build();
       ApiService apiService = retrofit.create(ApiService.class);
       //请求
       Call<WeatherBean> weatherBeanCall = apiService.requestWeather(detailId);
       weatherBeanCall.enqueue(callback);
   }
}



4、再创建一个类，用来处理M层和V层之间的通信，也就是P层 



/**
 * @description P层
 * 特点:需要持有M层和V层
 */
public class RequestPresenter1 {
    private final RequestView1 mRequestView;
    private final RequestMode1 mRequestMode;
    public RequestPresenter1(RequestView1 requestView) {
        this.mRequestView = requestView;
        this.mRequestMode = new RequestMode1();
    }
    public void clickRequest(final String cityId){
        //请求时显示加载
        mRequestView.requestLoading();
        //模拟耗时，可以展示出loading
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                mRequestMode.request(cityId, new Callback<WeatherBean>() {
                    @Override
                    public void onResponse(Call<WeatherBean> call, Response<WeatherBean> response) {
                        mRequestView.resultSuccess(response.body());
                    }
                    @Override
                    public void onFailure(Call<WeatherBean> call, Throwable t) {
                        mRequestView.resultFailure(Log.getStackTraceString(t));
                    }
                });
            }
        },1000);
    }
}



好了，上面的4步就是最基本的MVP模式的使用了，可是这样写会内存泄露，因为如果在网络请求的过程中Activity就关闭了，Presenter还持有了V层的引用，也就是MainActivity，就会内存泄露。




下面就来解决这个问题，我们将P层和V层的关联抽出两个方法，一个绑定，一个解绑，在需要的时候进行绑定V层，不需要的时候进行解绑就可以了。


我们只需要修改上面Presenter中的构造代码，不需要在构造中传递V层了，然后再写一个绑定和解绑的方法，最后修改Activity创建Presenter时进行绑定，在onDestroy中进行解绑。


修改后的Presenter：


public class RequestPresenter2 {
    private RequestView2 mView;
    private RequestMode2 mMode;
    public RequestPresenter2() {
        mMode = new RequestMode2();
    }
    public void clickRequest(final String cityId) {
        if(mView != null){
            mView.requestLoading();
            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    mMode.request(cityId, new Callback<WeatherBean>() {
                        @Override
                        public void onResponse(Call<WeatherBean> call, Response<WeatherBean> response) {
                            if(mView != null){
                                mView.resultSuccess(response.body());
                            }
                        }
                        @Override
                        public void onFailure(Call<WeatherBean> call, Throwable t) {
                            if(mView != null){
                                mView.resultFailure(Log.getStackTraceString(t));
                            }
                        }
                    });
                }
            },1000);
        }
    }
    /**
     * 绑定
     * @param view
     */
    public void attach( RequestView2 view) {
        this.mView = view;
    }
    /**
     * 解除绑定
     */
    public void detach() {
        mView = null;
    }
    /**
     * 取消网络请求
     */
    public void interruptHttp(){
        mMode.interruptHttp();
    }
}



修改后的MainActivity： 



/**
 * 第三步：对应demo2
 * 上面的问题：
 * 1.是会内存泄露，因为persenter一直持有Activity，如果一个发了一个请求，
 * 但是网络有点慢，这个时候退出Activity，那么请求回来后还是会调用
 * Activity的回调方法，这里还是因为一直持有的问题
 * 2.如果已经退出了当前界面，这个请求也没有用了，这个时候我们可以断开请求
 * <p>
 * 解决问题：
 * 1.增加绑定和解绑的方法来解决内存泄露和退出后还会回调的问题
 * 2、增加断开网络连接的方法
 */
public class MainActivity extends AppCompatActivity implements RequestView2 {
    @FieldView(R.id.tv_text)
    private TextView textView;
    private RequestPresenter2 presenter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ViewFind.bind(this);
        presenter = new RequestPresenter2();
        presenter.attach(this);
    }
    public void request(View view) {
        presenter.clickRequest("101010100");
    }
    @Override
    public void requestLoading() {
        textView.setText("请求中,请稍后...");
    }
    @Override
    public void resultSuccess(WeatherBean result) {
        //成功
        textView.setText(result.getWeatherinfo().toString());
    }
    @Override
    public void resultFailure(String result) {
        //失败
        textView.setText(result);
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        presenter.detach();
        presenter.interruptHttp();
    }
}



这样我们就解决了内存泄露的问题，但是这样还是不完美，应用中肯定不可能只有一个模块，每个模块都对应着一个V层和P层，那这样的话每个Presenter中都要定义绑定和解绑的方法，而Activity中对应的也要调用这绑定和解绑的两个方法，代码冗余。


5简单抽象-解决MVP代码冗余


针对这个问题我们可以抽取出一个基类的Presenter和一个基类的Activity来做这个事情，让子类不用在写这些重复的代码。但是问题又来了，既然是基类，肯定不止有一个子类来继承基类，那么也就是说子类当中定义的View接口和需要创建的Presenter都不相同，我们肯定在基类当中不能写死吧，那就使用泛型来设计。



思路： 


1.创建一个基类View，让所有View接口都必须实现,这个View可以什么都不做只是用来约束类型的


2.创建一个基类的Presenter，在类上规定View泛型，然后定义绑定和解绑的抽象方法，让子类去实现，对外在提供一个获取View的方法， 
让子类直接通过方法来获取View


3.创建一个基类的Activity，声明一个创建Presenter的抽象方法，因为要帮子类去绑定和解绑那么就需要拿到子类的Presenter才行，但是又不能随便一个类都能绑定的，因为只有基类的Presenter中才定义了绑定和解绑的方法，所以同样的在类上可以声明泛型在，方法上使用泛型来达到目的。


4.修改Presenter和Activity中的代码，各自继承自己的基类并去除重复代码


实现步骤：


1.创建一个基类View，让所有View接口都必须实现 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description 所有mvpView的父接口
 */
public interface IMvpBaseView4 {
}



2.创建一个基类的Presenter，在类上规定View泛型，然后定义绑定和解绑的方法，对外在提供一个获取View的方法，让子类直接通过方法来获取View使用即可 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description 指定绑定的View必须继承自IMvpBaseView4
 */
public abstract class AbstractMvpPersenter4<V extends IMvpBaseView4> {
    private V mMvpView;
    /**
     * 绑定V层
     * @param view
     */
    public void attachMvpView(V view){
        this.mMvpView = view;
    }
    /**
     * 解除绑定V层
     */
    public void detachMvpView(){
        mMvpView = null;
    }
    /**
     * 获取V层
     * @return
     */
    public V getmMvpView() {
        return mMvpView;
    }
}



3.创建一个基类的Activity，声明一个创建Presenter的抽象方法，因为要帮子类去绑定和解绑那么就需要拿到子类的Presenter才行，但是又不能随便一个类都能绑定的，因为只有基类的Presenter中才定义了绑定和解绑的方法，所以同样的在类上可以声明泛型在方法上使用泛型来达到目的 



/**
 * @description MvpActivity
 * 指定子类具体的View必须继承自IMvpBaseView4
 * 指定子类具体的Presenter必须继承自AbstractMvpPersenter4
 */
public abstract class AbstractMvpActivity<V extends IMvpBaseView4, P extends AbstractMvpPersenter4<V>> 
                   extends AppCompatActivity implements IMvpBaseView4 {
    private P presenter;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //创建Presenter
        if (presenter == null) {
            presenter = createPresenter();
        }
        if (presenter == null) {
            throw new NullPointerException("presenter 不能为空!");
        }
        //绑定view
        presenter.attachMvpView((V) this);
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        //解除绑定
        if (presenter != null) {
            presenter.detachMvpView();
        }
    }
    /**
     * 创建Presenter
     * @return 子类自己需要的Presenter
     */
    protected abstract P createPresenter();
    /**
     * 获取Presenter
     * @return 返回子类创建的Presenter
     */
    public P getPresenter() {
        return presenter;
    }
}



4.修改Presenter和Activity中的代码，各自继承自己的基类并去除重复代码
修改后的Presenter: 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description P层
 */
public class RequestPresenter4 extends AbstractMvpPersenter4<RequestView4> {
    private final RequestMode4 mRequestMode;
    public RequestPresenter4() {
        this.mRequestMode = new RequestMode4();
    }
    public void clickRequest(final String cityId){
        //获取View
        if(getmMvpView() != null){
            getmMvpView().requestLoading();
        }
        //模拟网络延迟，可以显示出加载中
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                mRequestMode.request(cityId, new Callback<WeatherBean>() {
                    @Override
                    public void onResponse(Call<WeatherBean> call, Response<WeatherBean> response) {
                        //判断View是否为空
                        if(getmMvpView() != null){
                            getmMvpView().resultSuccess(response.body());
                        }
                    }
                    @Override
                    public void onFailure(Call<WeatherBean> call, Throwable t) {
                        if(getmMvpView() != null){
                            getmMvpView().resultFailure(Log.getStackTraceString(t));
                        }
                    }
                });
            }
        },1000);
    }
    public void interruptHttp(){
        mRequestMode.interruptHttp();
    }
}



修改后的Activity： 



public class MainActivity extends AbstractMvpActivity<RequestView4, RequestPresenter4> implements RequestView4 {
    @FieldView(R.id.tv_text)
    private TextView textView;
    private RequestPresenter3 presenter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ViewFind.bind(this);
    }
    @Override
    protected RequestPresenter4 createPresenter() {
        return new RequestPresenter4();
    }
    //点击事件
    public void request(View view) {
        getPresenter().clickRequest("101010100");
    }
    @Override
    public void requestLoading() {
        textView.setText("请求中,请稍后...");
    }
    @Override
    public void resultSuccess(WeatherBean result) {
        //成功
        textView.setText(result.getWeatherinfo().toString());
    }
    @Override
    public void resultFailure(String result) {
        //失败
        textView.setText(result);
    }
}   



到这里完美了吗？没有，还可以再抽，来分析一下还有哪些不完美的地方以及如何再优化。




高级抽象-使用注解、工厂模式、代理模式、策略模式整体解决代码冗余、内存泄露、Presenter生命周期以及数据存储问题



1.每个子类都要重写父类创建Presenter的方法，创建一个Presenter并返回，这一步我们也可以让父类帮忙干了，怎么做呢？


我们可以采用注解的方式，在子类上声明一个注解并注明要创建的类型，剩下的事情就让父类去做了,但是父类得考虑如果子类不想这么干怎么办，那也还是不能写死吧，可以使用策略模式加工厂模式来实现，我们默认使用这种注解的工厂 ，但是如果子类不喜欢可以通过父类提供的一个方法来创建自己的工厂。


2.Presenter真正的创建过程，我们可以将它放到真正使用Presenter的时候再创建，这样的话可以稍微优化一下性能问题


3.界面有可能会意外销毁并重建，Activity、Fragment、View都可以在销毁的时候通过onDestroy释放一些资源并在onSaveInstanceState方法中存储一些数据然后在重建的时候恢复，但是有可能Presenter中也需要释放一些资源存储一些数据，那么上面的结构就不能满足了，我们可以给Presenter增加生命周期的方法，让Presenter和V层生命周期同步就可以做到了


4.第三步中我们又给Presenter加入了一些生命周期的方法，再加上Presenter的创建绑定和解绑的方法，那么如果我们在创建一个MvpFragment基类，或者View的基类那么这么多的代码岂不是都要copy一份吗，而且看起来也很不清晰，这里我们可以采用代理模式来优化一下。


好了下面来实现：



1.我们既然要采用工厂模式才创建Presenter，那么我们首先来创建一个工厂接口


/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description Presenter工厂接口
 */
public interface PresenterMvpFactory<V extends BaseMvpView,P extends BaseMvpPresenter<V>> {
    /**
     * 创建Presenter的接口方法
     * @return 需要创建的Presenter
     */
    P createMvpPresenter();
}



2.然后我们需要创建一个默认使用注解创建的工厂，那么首先要创建一个注解


注解： 



/**
 * @description 标注创建Presenter的注解
 */
@Inherited
@Retention(RetentionPolicy.RUNTIME)
public @interface CreatePresenter {
    Class<? extends BaseMvpPresenter> value();
}



注解工厂： 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description Presenter工厂实现类
 */
public class PresenterMvpFactoryImpl<V extends BaseMvpView, P extends BaseMvpPresenter<V>> implements PresenterMvpFactory<V, P> {
    /**
     * 需要创建的Presenter的类型
     */
    private final Class<P> mPresenterClass;
    /**
     * 根据注解创建Presenter的工厂实现类
     * @param viewClazz 需要创建Presenter的V层实现类
     * @param <V> 当前View实现的接口类型
     * @param <P> 当前要创建的Presenter类型
     * @return 工厂类
     */
    public static <V extends BaseMvpView, P extends BaseMvpPresenter<V>> PresenterMvpFactoryImpl<V,P> createFactory(Class<?> viewClazz){
        CreatePresenter annotation = viewClazz.getAnnotation(CreatePresenter.class);
        Class<P> aClass = null;
        if(annotation != null){
            aClass = (Class<P>) annotation.value();
        }
        return aClass == null ? null : new PresenterMvpFactoryImpl<V, P>(aClass);
    }
    private PresenterMvpFactoryImpl(Class<P> presenterClass) {
        this.mPresenterClass = presenterClass;
    }
    @Override
    public P createMvpPresenter() {
        try {
            return mPresenterClass.newInstance();
        } catch (Exception e) {
            throw new RuntimeException("Presenter创建失败!，检查是否声明了@CreatePresenter(xx.class)注解");
        }
    }
}



3.我们说了不能写死这个工厂，那么我们需要使用者可以自定义，那么我们还需要给使用者提供一个设置的方法，我们定义一个接口提供设置工厂、获取工厂、获取Presenter的方法，然后让V层来实现这个接口，这样V层的子类就可以通过相应的方法使用了 



/**
 * @author 刘镓旗
 * @date 2017/11/20
 * @description 代理接口
 */
public interface PresenterProxyInterface<V extends BaseMvpView,P extends BaseMvpPresenter<V>> {
    /**
     * 设置创建Presenter的工厂
     * @param presenterFactory PresenterFactory类型
     */
    void setPresenterFactory(PresenterMvpFactory<V,P> presenterFactory);
    /**
     * 获取Presenter的工厂类
     * @return 返回PresenterMvpFactory类型
     */
    PresenterMvpFactory<V,P> getPresenterFactory();
    /**
     * 获取创建的Presenter
     * @return 指定类型的Presenter
     */
    P getMvpPresenter();
}



4.给Presenter增加生命周期的方法 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description 所有Presenter的基类，并不强制实现这些方法，有需要在重写
 */
public class BaseMvpPresenter<V extends BaseMvpView> {
    /**
     * V层view
     */
    private V mView;
    /**
     * Presenter被创建后调用
     *
     * @param savedState 被意外销毁后重建后的Bundle
     */
    public void onCreatePersenter(@Nullable Bundle savedState) {
        Log.e("perfect-mvp","P onCreatePersenter = ");
    }
    /**
     * 绑定View
     */
    public void onAttachMvpView(V mvpView) {
        mView = mvpView;
        Log.e("perfect-mvp","P onResume");
    }
    /**
     * 解除绑定View
     */
    public void onDetachMvpView() {
        mView = null;
        Log.e("perfect-mvp","P onDetachMvpView = ");
    }
    /**
     * Presenter被销毁时调用
     */
    public void onDestroyPersenter() {
        Log.e("perfect-mvp","P onDestroy = ");
    }
    /**
     * 在Presenter意外销毁的时候被调用，它的调用时机和Activity、Fragment、View中的onSaveInstanceState
     * 时机相同
     *
     * @param outState
     */
    public void onSaveInstanceState(Bundle outState) {
        Log.e("perfect-mvp","P onSaveInstanceState = ");
    }
    /**
     * 获取V层接口View
     *
     * @return 返回当前MvpView
     */
    public V getMvpView() {
        return mView;
    }
}



5.创建一个代理来管理Presenter的生命周期方法 



/**
 * @author 刘镓旗
 * @date 2017/11/20
 * @description 代理实现类，用来管理Presenter的生命周期，还有和view之间的关联
 */
public class BaseMvpProxy<V extends BaseMvpView, P extends BaseMvpPresenter<V>> implements PresenterProxyInterface<V, P>{
    /**
     * 获取onSaveInstanceState中bundle的key
     */
    private static final String PRESENTER_KEY = "presenter_key";
    /**
     * Presenter工厂类
     */
    private PresenterMvpFactory<V, P> mFactory;
    private P mPresenter;
    private Bundle mBundle;
    private boolean mIsAttchView;
    public BaseMvpProxy(PresenterMvpFactory<V, P> presenterMvpFactory) {
        this.mFactory = presenterMvpFactory;
    }
    /**
     * 设置Presenter的工厂类,这个方法只能在创建Presenter之前调用,也就是调用getMvpPresenter()之前，如果Presenter已经创建则不能再修改
     *
     * @param presenterFactory PresenterFactory类型
     */
    @Override
    public void setPresenterFactory(PresenterMvpFactory<V, P> presenterFactory) {
        if (mPresenter != null) {
            throw new IllegalArgumentException("这个方法只能在getMvpPresenter()之前调用，如果Presenter已经创建则不能再修改");
        }
        this.mFactory = presenterFactory;
    }
    /**
     * 获取Presenter的工厂类
     *
     * @return PresenterMvpFactory类型
     */
    @Override
    public PresenterMvpFactory<V, P> getPresenterFactory() {
        return mFactory;
    }
    /**
     * 获取创建的Presenter
     *
     * @return 指定类型的Presenter
     * 如果之前创建过，而且是以外销毁则从Bundle中恢复
     */
    @Override
    public P getMvpPresenter() {
        Log.e("perfect-mvp","Proxy getMvpPresenter");
        if (mFactory != null) {
            if (mPresenter == null) {
                mPresenter = mFactory.createMvpPresenter();
                mPresenter.onCreatePersenter(mBundle == null ? null : mBundle.getBundle(PRESENTER_KEY));
            }
        }
        Log.e("perfect-mvp","Proxy getMvpPresenter = " + mPresenter);
        return mPresenter;
    }
    /**
     * 绑定Presenter和view
     * @param mvpView
     */
    public void onResume(V mvpView) {
        getMvpPresenter();
        Log.e("perfect-mvp","Proxy onResume");
        if (mPresenter != null && !mIsAttchView) {
            mPresenter.onAttachMvpView(mvpView);
            mIsAttchView = true;
        }
    }
    /**
     * 销毁Presenter持有的View
     */
    private void onDetachMvpView() {
        Log.e("perfect-mvp","Proxy onDetachMvpView = ");
        if (mPresenter != null && mIsAttchView) {
            mPresenter.onDetachMvpView();
            mIsAttchView = false;
        }
    }
    /**
     * 销毁Presenter
     */
    public void onDestroy() {
        Log.e("perfect-mvp","Proxy onDestroy = ");
        if (mPresenter != null ) {
            onDetachMvpView();
            mPresenter.onDestroyPersenter();
            mPresenter = null;
        }
    }
    /**
     * 意外销毁的时候调用
     * @return Bundle，存入回调给Presenter的Bundle和当前Presenter的id
     */
    public Bundle onSaveInstanceState() {
        Log.e("perfect-mvp","Proxy onSaveInstanceState = ");
        Bundle bundle = new Bundle();
        getMvpPresenter();
        if(mPresenter != null){
            Bundle presenterBundle = new Bundle();
            //回调Presenter
            mPresenter.onSaveInstanceState(presenterBundle);
            bundle.putBundle(PRESENTER_KEY,presenterBundle);
        }
        return bundle;
    }
    /**
     * 意外关闭恢复Presenter
     * @param savedInstanceState 意外关闭时存储的Bundler
     */
    public void onRestoreInstanceState(Bundle savedInstanceState) {
        Log.e("perfect-mvp","Proxy onRestoreInstanceState = ");
        Log.e("perfect-mvp","Proxy onRestoreInstanceState Presenter = " + mPresenter);
        mBundle = savedInstanceState;
    }
}



6.最后V层实现，首先实现设置工厂的接口，然后创建一个代理并传入默认工厂，在V层生命周期中使用代理去实现管理Presenter的生命周期 



/**
 * @author 刘镓旗
 * @date 2017/11/17
 * @description 继承自Activity的基类MvpActivity
 * 使用代理模式来代理Presenter的创建、销毁、绑定、解绑以及Presenter的状态保存,其实就是管理Presenter的生命周期
 */
public abstract class AbstractMvpActivitiy<V extends BaseMvpView, P extends BaseMvpPresenter<V>> extends Activity implements PresenterProxyInterface<V,P> {
    private static final String PRESENTER_SAVE_KEY = "presenter_save_key";
    /**
     * 创建被代理对象,传入默认Presenter的工厂
     */
    private BaseMvpProxy<V,P> mProxy = new BaseMvpProxy<>(PresenterMvpFactoryImpl.<V,P>createFactory(getClass()));
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.e("perfect-mvp","V onCreate");
        Log.e("perfect-mvp","V onCreate mProxy = " + mProxy);
        Log.e("perfect-mvp","V onCreate this = " + this.hashCode());
        if(savedInstanceState != null){
            mProxy.onRestoreInstanceState(savedInstanceState.getBundle(PRESENTER_SAVE_KEY));
        }
    }
    @Override
    protected void onResume() {
        super.onResume();
        Log.e("perfect-mvp","V onResume");
        mProxy.onResume((V) this);
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.e("perfect-mvp","V onDestroy = " );
        mProxy.onDestroy();
    }
    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        Log.e("perfect-mvp","V onSaveInstanceState");
        outState.putBundle(PRESENTER_SAVE_KEY,mProxy.onSaveInstanceState());
    }
    @Override
    public void setPresenterFactory(PresenterMvpFactory<V, P> presenterFactory) {
        Log.e("perfect-mvp","V setPresenterFactory");
        mProxy.setPresenterFactory(presenterFactory);
    }
    @Override
    public PresenterMvpFactory<V, P> getPresenterFactory() {
        Log.e("perfect-mvp","V getPresenterFactory");
        return mProxy.getPresenterFactory();
    }
    @Override
    public P getMvpPresenter() {
        Log.e("perfect-mvp","V getMvpPresenter");
        return mProxy.getMvpPresenter();
    }
}



最后看一下使用，首先在V层上定义需要创建的Presenter，声明自己模块具体的View接口类型和Presenter类型，最后实现自己View接口就ok了，还有就是如果要设置自己的Presenter创建工厂，必须在调用onResume方法和getMvpPresenter方法之前设置 



//声明需要创建的Presenter
@CreatePresenter(RequestPresenter5.class)
public class MainActivity extends AbstractMvpAppCompatActivity<RequestView5, RequestPresenter5> implements RequestView5 {
    @FieldView(R.id.tv_text)
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ViewFind.bind(this);
        //设置自己的Presenter工厂，如果你想自定义的话
        // setPresenterFactory(xxx);
        if(savedInstanceState != null){
            Log.e("perfect-mvp","MainActivity  onCreate 测试  = " + savedInstanceState.getString("test") );
        }
    }
    //点击事件
    public void request(View view) {
        Log.e("perfect-mvp","点击事件");
        getMvpPresenter().clickRequest("101010100");
    }
    @Override
    public void requestLoading() {
        textView.setText("请求中,请稍后...");
    }
    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        Log.e("perfect-mvp","MainActivity onSaveInstanceState 测试");
        outState.putString("test","test_save");
    }
    @Override
    public void resultSuccess(WeatherBean result) {
        //成功
        textView.setText(result.getWeatherinfo().toString());
    }
    @Override
    public void resultFailure(String result) {
        //失败
        textView.setText(result);
    }
}   



这时候如果界面意外销毁,Presenter可以通过重写以下方法进行释放资源，存储数据，和恢复数据，例如：



@Override
public void onCreatePersenter(@Nullable Bundle savedState) {
    super.onCreatePersenter(savedState);
    if(savedState != null){
        Log.e("perfect-mvp","RequestPresenter5  onCreatePersenter 测试  = " + savedState.getString("test2") );
    }
}
@Override
public void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    Log.e("perfect-mvp","RequestPresenter5  onSaveInstanceState 测试 " );
    outState.putString("test2","test_save2");
}
@Override
public void onDestroyPersenter() {
    super.onDestroyPersenter();
}



哦了！大功告成，perfect！可能有的人会说这只是Activity，那么Fragment中怎么弄呢，其实是一模一样的，我们将实现全部抽离到了 代理中，那么Fragment中也只需要创建一个代理，然后在生命周期中使用代理调用相应就好。


当然最后我的库中已经实现了Fragment的基类和AppCompatActivity的基类，至于View的如果有使用到的可以自行扩展，再次声明本文只是提供一种思路和封装的方法，并不代表就是最好的，如果有更好的想法和思路可以一起探讨。


最后奉上github地址，还希望可以给个star鼓励一下。再次感谢！


GitHub地址：
https://github.com/ljqloveyou123
