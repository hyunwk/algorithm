function solution(participant, completion) {
    participant.sort();
    completion.sort();
      
    let i = 0;
    while (participant[i] === completion[i])
        i++;
    let answer = participant[i];
    return answer;
}
