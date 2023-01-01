import org.junit.jupiter.api.Test;

import java.util.HashSet;

public class findStudent_1 {
    public int solution(int[] nums) {
        // 최대 선택 가능 수
        int numsLength = nums.length / 2;

        HashSet<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            hashSet.add(num);
        }
        // 중복 제거 후 요소 개수
        int removeDuplicateNumsLength = hashSet.size();

        if (removeDuplicateNumsLength > numsLength) {
            return numsLength;
        }
        return removeDuplicateNumsLength;
    }
}
