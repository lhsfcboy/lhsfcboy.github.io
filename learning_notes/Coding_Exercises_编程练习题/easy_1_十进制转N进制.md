# 十进制转N进制

请读者自由设定具体限制，例如不考虑小数，不考虑负数等条件。

## 参考实现

```java
public class DecimalBaseConverter {
    private static final String DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    /**
     * 将十进制数转换为指定进制的字符串表示
     * @param decimal 待转换的十进制数
     * @param base 目标进制（2-36）
     * @return 转换后的字符串
     * @throws IllegalArgumentException 当进制base不在2-36范围内时抛出
     */
    public static String convert(int decimal, int base) {
        // 检查进制范围是否有效
        if (base < 2 || base > 36) {
            throw new IllegalArgumentException("进制必须在2到36之间");
        }
        
        // 处理0的特殊情况
        if (decimal == 0) {
            return "0";
        }
        
        // 处理负数
        boolean isNegative = decimal < 0;
        decimal = Math.abs(decimal);
        
        StringBuilder result = new StringBuilder();
        
        // 进行进制转换
        while (decimal > 0) {
            result.insert(0, DIGITS.charAt(decimal % base));
            decimal = decimal / base;
        }
        
        // 如果是负数，添加负号
        if (isNegative) {
            result.insert(0, '-');
        }
        
        return result.toString();
    }
    
    /**
     * 测试方法
     */
    public static void main(String[] args) {
        // 测试例子
        System.out.println("10进制 15 转 2进制: " + convert(15, 2));  // 1111
        System.out.println("10进制 15 转 8进制: " + convert(15, 8));  // 17
        System.out.println("10进制 15 转 16进制: " + convert(15, 16)); // F
        System.out.println("10进制 -15 转 16进制: " + convert(-15, 16)); // -F
        
        try {
            System.out.println("无效进制测试: " + convert(15, 37));
        } catch (IllegalArgumentException e) {
            System.out.println("错误: " + e.getMessage());
        }
    }
}

```
