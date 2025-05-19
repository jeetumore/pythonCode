
import boto3




# def dowloadafile():
#
#     bucket_name = "paid-search-data"
#     pathtofile = "reports/Exception/Exception2024-04-17.csv"
#     localpath = 'download.txt'
#     s3 = boto3.client("s3")
#     try:
#         s3.download_file(bucket_name, pathtofile, localpath)
#         print("file has been downloaded: {localpath}")
#     except Exception as e:
#         print("Error in downloading, {e}")
#
# # s3 = boto3.resource("s3")
# dowloadafile()



# def downloadFileInChunck():
#     bucket_name = "paid-search-data"
#     pathtofile = "reports/Exception/Exception2024-04-17.csv"
#     localpath = 'download1.txt'
#     chunk_size = 1024 * 1024
#
#     s3 = boto3.client("s3")
#     try:
#         response = s3.get_object(Bucket=bucket_name, Key=pathtofile)
#         with open(localpath, "wb") as file:
#             for chunk in response["Body"].iter_chunks(chunk_size):
#                 if chunk:
#                     file.write(chunk)
#
#         print("file has been downloaded")
#     except Exception as e:
#         print("error {e}")
#
#
# downloadFileInChunck()






# def dowloadFileusingchunk():
#     bucket_name = "paid-search-data"
#     pathtofile = "reports/Exception/Exception2024-04-17.csv"
#     localpath = 'download1.txt'
#     chunk_size = 1024
#
#     s3 = boto3.client("s3")
#     try:
#         response = s3.get_object(Bucket=bucket_name, Key=pathtofile)
#         with open(localpath, "wb") as file:
#             for chunk in response["Body"].iter_chunks(chunk_size):
#                 if chunk:
#                     file.write(chunk)
#
#         print(f"file has been download successfully {localpath}")
#
#     except Exception as e:
#         print(f"error: {e}")
#
# dowloadFileusingchunk()




import requests


def downloadfile(url, chuncksize):

    response = requests.get(url)

    with open("zipfile.png", "wb") as file:
        for chunk in response.iter_content(chuncksize):
            if chunk:
                file.write(chunk)


    print("file has been downloaded ")

downloadfile("http://localhost:8000/Downloads/1000069704.jpg", 1024)




def downloadfile(url, chunksize):


    try:
        response = requests.get(url)
        with open("newfile.jpg", "w") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)


    except Exception as e:
        print(f"error: {e}")


        print("file has been dowload successfully")

downloadfile("http://localhost:8000/Downloads/10000697101wsss4.jpg", 1024)




#
#
# import requests
#
#
# resp = requests.get(url="zipfileurl", stream=True):
# with open("downloadfile", 'wb') as file:
#     for chunk in resp.iter_content(chunk_size=1024):
#         if chunk:
#             file.write(chunk)









