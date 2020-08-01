// new keyword for object instantiation
MyClass myJavaObject = new MyClass();


// Constructor
public class MyClass{
    int x;
    int y;

    public MyClass(/*this*/, int x, int y) {
        this.x = x;
        this.y = y;
    }
}

// Private Fields
class JavaPrivateClass {
    private x = 'private enforced by language';
}