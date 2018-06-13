import argparse
import face_recognition
import glob
import os


def main(path_to_images):
    files_list = glob.glob(os.path.join(path_to_images, '*.png'))
    files_list += glob.glob(os.path.join(path_to_images, '*.jpg'))
    for image in files_list:
        image = face_recognition.load_image_file(image)
        face_landmarks_list = face_recognition.face_landmarks(image)
        print(face_landmarks_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Align and crop your images!')
    parser.add_argument('path_to_images', help='full path to your images')
    parser.add_argument('output_path', help='full output path')
    args = parser.parse_args()

    main(args.path_to_images)
