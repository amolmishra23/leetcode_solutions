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

// using merge sort - divide and conquer (O(nlogn) and O(1))
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) {
            // base case if empty list is given input
            return head;
        }
        
        auto slow = head, fast = head;
        // we are going to split the list into 2 halves
        while(fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        fast = slow;
        // slow is the start of the second LL
        slow = slow->next;
        fast->next = nullptr;
        
        // we assume to have sorted list as output from the half half list
        // and then we merge them, using the merge sort way
        return merge_list(sortList(head), sortList(slow));
    }
    
    ListNode* merge_list(ListNode* l1, ListNode *l2) {
        // a new sorted list we create here
        ListNode dummy{0};
        auto curr = &dummy;
        
        // whichever element is smaller we keep adding it to the sorted list!
        while (l1 && l2) {
            if (l1->val<=l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        
        curr->next = l1 ? l1 : l2;
        
        return dummy.next;
    }
};