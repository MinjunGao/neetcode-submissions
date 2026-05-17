class LinkedList {
public:

    struct ListNode {
        int val;
        ListNode* next;
        ListNode(int val): val(val), next(nullptr){}
    };

    LinkedList() {
        _dummy = new ListNode(-1);
        _tail = _dummy;
    }

    int get(int index) {
        int i = 0;
        ListNode* curr = _dummy;
        while (i <= index) {
            curr = curr->next;
            if (curr == nullptr) {
                return -1;
            }
            ++i;
        }
        return curr->val;
    }

    void insertHead(int val) {
        ListNode* new_head = new ListNode(val);
        new_head->next = _dummy->next;
        _dummy->next = new_head;
        if (new_head->next == nullptr) {
            _tail = new_head;
        }
    }
    
    void insertTail(int val) {
        ListNode* new_tail = new ListNode(val);
        _tail->next = new_tail;
        _tail = new_tail;
    }

    bool remove(int index) {
        int i = 0;
        ListNode* curr = _dummy;
        ListNode* prev = curr;
        while (i <= index) {
            prev = curr;
            curr = curr->next;
            if (curr == nullptr) {
                return false;
            }
            ++i;
        }
        if (curr == _tail) {
            _tail = prev;
        }
        prev->next = curr->next;
        return true;
    }

    vector<int> getValues() {
        vector<int> vals;
        ListNode* curr = _dummy->next;
        while (curr != nullptr) {
            vals.push_back(curr->val);
            curr = curr->next;
        }
        return vals;
    }

private:
    ListNode* _dummy;
    ListNode* _tail;
};
