/*
Definition of singly linked list:
struct ListNode
{
    int val;
    ListNode *next;
    ListNode()
    {
        val = 0;
        next = NULL;
    }
    ListNode(int data1)
    {
        val = data1;
        next = NULL;
    }
    ListNode(int data1, ListNode *next1)
    {
        val = data1;
        next = next1;
    }
};
*/

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* temp = head;
        int cnt = 0;

        while(temp != NULL){
            cnt++;
            temp = temp->next;
        }
        if(n == 1){
            // delete last element
            if(cnt == 1){
                free(head);
                return NULL;
                }
            temp = head;
            while(cnt - 2 > 0){
                cnt--;
                temp = temp->next;
            }
            ListNode* delNode = temp->next;
            temp->next = NULL;
            free(delNode);
            return head;
        }
        if(n == cnt){
            // delete first element
            temp = head;
            head = head->next;
            free(temp);
            return head;
        }
        // delete middle element
        temp = head;
        for(int i = 1; i < cnt - n ; i++){
            temp = temp->next;
        }
        ListNode* delNode = temp->next;

        temp->next = temp->next->next;
        free(delNode);

        return head;

    }
};