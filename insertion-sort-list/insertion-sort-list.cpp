/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        /*
        Performing it the actual insertion sort way
        Have a dummy list with INT_MIN created. 
        Iterate through the entire list, and search each node's position to be inserted in the new list. 
        And manupulate the pointers, to insert it in the right location. 
        */
        ListNode dummy(INT_MIN);
        auto curr = head;
        ListNode *position = nullptr;
        
        while(curr) {
            position = get_insertion_position(&dummy, curr->val);
            ListNode* temp = curr->next;
            curr->next = position->next;
            position->next = curr;
            curr = temp;
        }
        
        return dummy.next;
    }
    
    ListNode* get_insertion_position(ListNode* head, int x) {
        ListNode* prev = nullptr;
        
        // iterating to the node, until we find the node, which is greater than the value of the current node
        for (auto curr = head; curr && curr->val<x; prev = curr, curr = curr->next);
        
        return prev;
    }
};