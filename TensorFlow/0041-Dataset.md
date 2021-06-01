# Dataset

如果需要训练的数据大小不大，例如不到1G，那么可以直接全部读入内存中进行训练，这样一般效率最高。
数据量很大时，使用tf.data API 可以构建数据输入管道，轻松处理大量的数据，不同的数据格式，以及不同的数据转换。

可以从 
1. Numpy array
2. Pandas DataFrame
3. Python generator
4. csv文件
5. 文本文件
6. 文件路径
7. tfrecords文件，对样本构建tf.Example后压缩成字符串写到tfrecoreds文件，读取后再解析成tf.Example。tfrecoreds文件的优点是压缩后文件较小，便于网络传播，加载速度较快。

等方式构建数据管道。


## 从Numpy array构建数据管道

```python
iris = datasets.load_iris()
ds1 = tf.data.Dataset.from_tensor_slices((iris["data"],iris["target"]))
for features,label in ds1.take(5):
    print(features,label)
```

## 从Pandas DataFrame构建数据管道

```python
iris = datasets.load_iris()
dfiris = pd.DataFrame(iris["data"],columns = iris.feature_names)
ds2 = tf.data.Dataset.from_tensor_slices((dfiris.to_dict("list"),iris["target"]))

for features,label in ds2.take(3):
    print(features,label)
```

## 从Python generator构建数据管道

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 定义一个从文件中读取图片的generator
image_generator = ImageDataGenerator(rescale=1.0/255).flow_from_directory(
                    "data/cifar2/test/",
                    target_size=(32, 32),
                    batch_size=20,
                    class_mode='binary')

classdict = image_generator.class_indices
print(classdict)

def generator():
    for features,label in image_generator:
        yield (features,label)

ds3 = tf.data.Dataset.from_generator(generator,output_types=(tf.float32,tf.int32))
```

## 从csv文件构建管道

```python
ds4 = tf.data.experimental.make_csv_dataset(
      file_pattern = ["data/titanic/train.csv","data/titanic/test.csv"],
      batch_size=3, 
      label_name="Survived",
      na_value="",
      num_epochs=1,
      ignore_errors=True)

for data,label in ds4.take(2):
    print(data,label)
```

## 从文本文件构建管道

```python
ds5 = tf.data.TextLineDataset(
    filenames = ["data/titanic/train.csv","data/titanic/test.csv"]
    ).skip(1) #略去第一行header

for line in ds5.take(5):
    print(line)
```
