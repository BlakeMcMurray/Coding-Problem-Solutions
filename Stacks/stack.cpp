#include <iostream>
#include <string>
using namespace std;
struct Node{
    string data;
    Node *next;
};

class Stack {
    public:
        Stack(); //constructor
        ~Stack(); //destructor
        void push(string elem); //pushes elem on top of stack
        string pop(); //pop top node off stack
        string toString(); // displays contents of stack as a single string
    private:
        Node *top;
        int height;

};

Stack::Stack(){
    top = NULL;
    height = 0;

}
Stack::~Stack(){
    //deconstructor to delete
    while(top != NULL){
        pop();
    }
    
}

void Stack::push(string elem){
    Node *temp = new Node;
    temp->data = elem;
    temp->next = top;
    height++;
    top = temp;

}

string Stack::pop(){
    if(top != NULL){
        string s = top->data;
        Node *old_top = top;
        top = top->next;
        delete old_top;
        height--;
        return s;
    }
    else{
        return "Nothing in Stack";
    }
}

string Stack::toString(){
    string s = "";
    Node *temp = top;
    while(temp){
        s += temp->data;
        temp = temp->next;
    }
    return s;
}


int main()
{   
    Stack *s = new Stack();
    s->push("first");
    s->push("second");
    cout << s->toString() << endl;
    cout << s->pop() << endl;
    cout << s->toString() << endl;

    delete s;
    return 0;

}
