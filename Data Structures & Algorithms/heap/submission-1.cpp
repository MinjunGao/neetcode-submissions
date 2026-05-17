class MinHeap {
public:
    MinHeap() {
        _min_heap.push_back(0);
    }

    void push(int val) {
        _min_heap.push_back(val);
        perculate_up(_min_heap.size() - 1);
    }

    int pop() {
        if (_min_heap.size() <= 1) {
            return -1;
        }
        int res = _min_heap[1];
        swap(1, _min_heap.size() - 1);
        _min_heap.pop_back();
        if (_min_heap.size() == 1) {
            return res;
        }
        perculate_down(1);
        return res;
    }

    int top() {
        if (_min_heap.size() <= 1) {
            return -1;
        }
        return _min_heap[1];
    }

    void heapify(const vector<int>& arr) {
        _min_heap.clear();
        _min_heap.push_back(0);
        _min_heap.insert(_min_heap.end(), arr.begin(), arr.end());
        for (int i = (_min_heap.size() - 1) / 2; i >= 1; --i) {
            perculate_down(i);
        }
    }

private:
    vector<int> _min_heap;

    int parent(int root) {
        return root / 2;
    }

    int left(int root) {
        return root * 2;
    }

    int right(int root) {
        return root * 2 + 1;
    }

    int is_greater(int i, int j) {
        return _min_heap[i] > _min_heap[j];
    }

    void swap(int i, int j) {
        int temp = _min_heap[i];
        _min_heap[i] = _min_heap[j];
        _min_heap[j] = temp;
    }

    void perculate_up(int root) {
        while (root > 1 && is_greater(parent(root), root)) {
            swap(parent(root), root);
            root = parent(root);
        }
    }

    void perculate_down(int root) {
        while (left(root) < _min_heap.size()) {
            int target = left(root);
            if (right(root) < _min_heap.size() && is_greater(target, right(root))) {
                target = right(root);
            }
            if (is_greater(target, root)) {
                break;
            }
            swap(target, root);
            root = target;
        }
    }
};
