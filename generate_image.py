import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
import numpy as np
from PIL import Image
import os

def load_model(sess, style):
    checkpoint_path = f'AnimeGANv2-1.0/checkpoint/generator_Hayao_weight/Hayao-64.ckpt'
    saver = tf.train.import_meta_graph(checkpoint_path + '.meta')
    saver.restore(sess, checkpoint_path)

    graph = tf.get_default_graph()

    input_image = graph.get_tensor_by_name("input_image:0")
    output_image = graph.get_tensor_by_name("output_image:0")

    return input_image, output_image

def generate_image(input_path, output_path, style):
    input_image = Image.open(input_path)
    input_image = input_image.convert("RGB")
    input_image = input_image.resize((256, 256))
    input_array = np.array(input_image)
    input_array = input_array / 127.5 - 1
    input_array = np.expand_dims(input_array, axis=0)

    with tf.Session() as sess:
        input_image_tensor, output_image_tensor = load_model(sess, style)
        output_image = sess.run(output_image_tensor, feed_dict={input_image_tensor: input_array})

        output_image = (output_image[0] + 1) * 127.5
        output_image = np.clip(output_image, 0, 255).astype(np.uint8)
        output_image = Image.fromarray(output_image)
        output_image.save(output_path)
