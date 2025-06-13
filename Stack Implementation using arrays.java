
class myStack{
    private int size;
    private int top;
    private int[] arr;  

    public myStack(int size){
        this.size = size;
        arr = new int[size];
        top = -1;
    }

    public boolean isEmpty(){
        return top == -1;

    }

    public void push(int val){
        if(top == size - 1){
            System.out.println("Memory overfolow, cannot insert more elements");
            return;
        }
        arr[++top] = val;
    }

    public int pop(){
        if(isEmpty()){
            System.out.println("No elements present in Stack");
            return -1;
        }
        else{
            int temp = arr[top--];
            return temp;
        }


    }

    public int peek(){
        if(isEmpty()){
            System.out.println("No elements present in Stack");
            return -1;
        }
        else return arr[top];

    }

    public void printStack(){
        if(isEmpty()) System.out.println("The Stack is empty");
        else{
            int temp = top;
            while(temp > 0){
                System.out.print(arr[temp--]+  "->");
            }
            System.out.println(arr[temp]);
        }
    }




    public static void main(String[] args) {
        myStack stack = new myStack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Top element is: " + stack.peek());
        stack.printStack();
        System.out.println("Popped element: " + stack.pop());
        stack.printStack();
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}