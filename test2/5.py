import tensorflow as tf

x_1 = tf.placeholder(tf.float32, name='x_1')
x_2 = tf.placeholder(tf.float32, name='x_2')
multiply = tf.multiply(x_1, x_2, name='multiply')
with tf.Session() as session:
    result = session.run(multiply, feed_dict={x_1: [1, 4, 9], x_2: [9, 4, 1]})

print(result)
