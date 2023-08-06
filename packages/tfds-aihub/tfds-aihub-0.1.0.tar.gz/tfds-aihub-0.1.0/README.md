# tfds aihub

AIhub 데이터를 tfrecord 형태로 GCS에 저장/캐싱하기 위한 코드.

## 데이터셋

### [K-Fashion Image(`k_fashion_image`)](https://aihub.or.kr/aidata/7988/download)

* Version: 1.1
* splits
    * `Training`: `967806`
    * `Validation`: `120975`
* Features:

        ```python
        tfds.features.FeaturesDict(
            {
                "image": tfds.features.Image(shape=(None, None, 3)),
                "objects": tfds.features.Sequence({
                    "type": tfds.features.ClassLabel(names=_BBOX_TYPE),
                    "bbox": tfds.features.BBoxFeature(),
                    "segmentation_mask": tfds.features.Image(shape=(None, None, 1)),
                    # TODO style 관련 정보
                })
            }
        )
        ```
