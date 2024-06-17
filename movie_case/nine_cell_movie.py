# -*- coding: utf-8 -*-
import os
import re
import shutil

from moviepy.editor import VideoFileClip, ImageSequenceClip, AudioFileClip
from PIL import Image

class MovieCase:

    def __init__(self):
        self.path_temp = './pics/'
        self.path_output = './output/'

        self.video_raw_clip = None
        self.video_width, self.video_height = None, None
        self.fps = None
        self.during = None
        self.item_space = 20

    @staticmethod
    def mkdir_folder(file_path):
        """
        创建一个文件夹，如果不存在就创建；否则不做处理
        :param file_path:
        :return:
        """
        if os.path.exists(file_path):
            return

        os.mkdir(file_path)

    @staticmethod
    def remove_folder(file_path):
        """
        删除文件夹
        :param file_path:
        :return:
        """
        shutil.rmtree(file_path)


    def get_audio_from_video(self, video_raw_clip, output_path):
        """
        从视频中提取音频
        :param video_raw_clip: 视频Clip对象
        :param output_path: 输出音频文件完整路径
        :return:
        """
        audio = video_raw_clip.audio
        audio.write_audiofile(output_path)
        return output_path

    @staticmethod
    def emb_numbers(s):
        re_digits = re.compile(r'(\d+)')
        pieces = re_digits.split(s)
        pieces[1::2] = map(int, pieces[1::2])
        return pieces

    def sort_strings_with_emb_numbers(self, alist) -> list:
        return sorted(alist, key=self.emb_numbers)

    def pics_to_video(self, pics_path, output_path, fps):
        """
        图片转为视频
        pics_to_video('./../gif_temp/', './../video_temp/temp1.mp4', 20)
        :param pics_path:
        :param output_path:
        :return:
        """
        image_paths = list(map(lambda x: pics_path + x, os.listdir(pics_path)))

        # 注意：这里必须进行一次排序，保证所有帧的顺序是一致
        image_paths = self.sort_strings_with_emb_numbers(image_paths)

        # 过滤掉非图片
        image_paths = list(filter(lambda image_path: image_path.endswith('.jpg'), image_paths))

        # 图片剪辑类
        clip = ImageSequenceClip(image_paths, fps=fps)
        clip.write_videofile(output_path)


    def video_with_audio(self, path_video_raw, path_bgm_raw, output):
        """
        视频合成音频
        :return:
        """
        videoclip = VideoFileClip(path_video_raw)
        audioclip = AudioFileClip(path_bgm_raw)

        # 设置视频音频，并写入到文件中去
        videoclip.set_audio(audioclip).write_videofile(output,
                                                       codec='libx264',
                                                       audio_codec='aac',
                                                       temp_audiofile='temp-audio.m4a',
                                                       remove_temp=True
                                                       )

    def execute(self):
        # 新建临时文件夹和输出文件夹
        self.mkdir_folder(self.path_temp)
        self.mkdir_folder(self.path_output)

        file_path = './test.mp4'
        self.video_raw_clip = VideoFileClip(file_path)
        # 宽、高
        self.video_width, self.video_height = self.video_raw_clip.w, self.video_raw_clip.h
        # 帧率
        self.fps = self.video_raw_clip.fps
        # 视频时长
        self.during = self.video_raw_clip.duration

        print(self.video_width, self.video_height, self.fps, self.during)
        file_index = 1
        for frame in self.video_raw_clip.iter_frames():
            image = Image.fromarray(frame)

            # 视频帧图片保存的临时路径（完整路径）
            frame_file_complete_path = self.path_temp + "%04d.jpg" % file_index
            file_index += 1

            # 1、剪成9张图片，计算每张图片的宽、高
            item_width = int(self.video_width / 3)
            item_height = int(self.video_height / 3)

            # 2、新的宽、高
            item_width_new = self.video_width + self.item_space * 2
            item_height_new = self.video_height + self.item_space * 2

            # 3、重新建一个画布背景
            new_image = Image.new(image.mode, (item_width_new, item_height_new), color='white')

            # 4、裁剪图片，然后粘贴到新的画布中去
            # i:横向、j：纵向
            for i in range(0, 3):
                for j in range(0, 3):
                    # 裁剪区域
                    box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)

                    # 根据区域，裁剪图片
                    crop_image = image.crop(box)

                    # 横向、纵向第2块和第3块，要加上偏移距离
                    x = 0 if j == 0 else (item_width + self.item_space) * j
                    y = 0 if i == 0 else (item_height + self.item_space) * i

                    # 将9张图片，按照上面计算的坐标值，粘贴到背景中去
                    new_image.paste(crop_image, (int(x), int(y)))

            # 保存图片到本地
            new_image.save(frame_file_complete_path)

        self.pics_to_video(self.path_temp, self.path_output + 'result.mp4', self.fps)

        self.remove_folder(self.path_temp)


if __name__ == '__main__':
    movie_case = MovieCase()
    movie_case.execute()
