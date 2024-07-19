# Reshape techniques view() vs reshape() vs permute() vs transpose()

## 1. view() vs reshape

> **view**: 오랫동안 지속되며 반환된 tensor는 원본 tensor와  data를 공유한다. 데이터의 순서를 유지시켜줌

> **reshape**: 원본 tensor의 복사본 또는 view를 반환. copy를 받을지 view를 받을지는 모른다.>

<br/><br/>

## 2. transpose() vs permute()

> **transpose**: 딱 두 개의 차원만 맞교환할 수 있다.

> **permute**: 모든 차원들을 맞교환할 수 있다.

<br/><br/>

## 3. view() vs permute()

> **view**: 모든 데이터의 순서를 유지시켜주며 차원을 변경해주고, contiguous를 유지시켜준다.

> **permute**: 해당하는 차원의 데이터도 함께 변경해주며 contiguous를 유지시켜주지 않는다.

<br/><br/>

## 4. 결론

- reshape과 view는 왠만하면 구분없이 써도 무방할 것 같지만 view를 쓰는게 더 안전할 것 같다.
- view연산과 permute연산은 아예 다르게 작용하기 때문에 feature차원이 아닌 input data차원에서는 어떤게 맞는지 확인하고 경계해서 사용해야 한다.
- permute를 사용하면 반드시 뒤에 .contiguous()를 붙여준다.
- view는 차원을 서로 붙이거나 떼어낼 때 사용하자. [B*2, C, D] -> [B, 2, C, D]
