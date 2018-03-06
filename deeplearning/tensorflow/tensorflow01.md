## tensorflow notes
```python
with tf.Session()as sess:
	with tf.device("/gpu:1"):
		x1 = tf.constant(5)
		x2 = tf.constant(6)
		outptu = tf.multiply(x1, x2)
```

