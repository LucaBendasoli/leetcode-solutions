from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}
        self.freq_to_keys = {}
    
    def _update_freq(self, key: int):
        val, freq = self.key_to_val_freq[key]
        
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        
        new_freq = freq + 1
        self.key_to_val_freq[key] = (val, new_freq)
        
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = OrderedDict()
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        val, freq = self.key_to_val_freq[key]
        self._update_freq(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_val_freq:
            val, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._update_freq(key)
            return
        
        if len(self.key_to_val_freq) >= self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
        
        self.key_to_val_freq[key] = (value, 1)
        self.min_freq = 1
        if 1 not in self.freq_to_keys:
            self.freq_to_keys[1] = OrderedDict()
        self.freq_to_keys[1][key] = None