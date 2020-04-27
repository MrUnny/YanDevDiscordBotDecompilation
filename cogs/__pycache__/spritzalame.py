# Python bytecode 3.7 (3394)
# Embedded file name: C:\Users\joelt\Desktop\aoi-bot\cogs\spritzalame.py
# Size of source mod 2**32: 3424 bytes
# Decompiled by https://python-decompiler.com
import asyncio, aiohttp, discord
from discord.ext import commands
from discord.ext.commands import BucketType
import subprocess, numpy, os
from utils import checks
from PIL import Image
from PIL import GifImagePlugin
from skimage.metrics import structural_similarity as ssim
userID = 0
percent = 0

def UserID(UID):
    global userID
    userID = UID


def percentNew(per):
    global percent
    percent = per


class ComparingShit:

    def __init__(self, image_a, image_b):
        self.image_a = image_a
        self.image_b = image_b

    def mse(self, image_a, image_b):
        """ Value of 0 for MSE indicates perfect similarity.
        A value greater than one implies less similarity and will continue
        to grow as the average difference between pixel intensities increases as well. """
        data = numpy.sum((image_a.astype('float') - image_b.astype('float')) ** 2)
        data /= float(image_a.shape[0] * image_a.shape[1])
        return data

    @property
    def compare_images(self):
        """ Returns MSE and SSIM value. SSIM returns in percentage of
        similarity while MSE returns float value where lower = more similar """
        m = round(self.mse(self.image_a, self.image_b), 4)
        s = round(ssim(self.image_a, self.image_b) * 100, 5)
        return (
         m, s)


class ConsumeFinder:

    def __init__(self):
        self.storage = []
        self.detected = False

    def detect(self):
        for g in self.storage:
            if match:
                self.detected = True


class spritzalame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    def on_message(self, message):
        if message.author.bot:
            return
        channel = self.bot.get_channel(685625174308945983)
        try:
            await message.attachments[0].save('lame/image.jpg')
        except:
            return
        else:
            for file in os.listdir('lamelist'):
                original = Image.open(f"lamelist/{file}").convert('L')
                w, h = original.size
                try:
                    comparing = Image.open('lame/image.jpg').convert('L').resize((w, h))
                except Image.DecompressionBombError:
                    return
                except:
                    return

                good_fucking_class = ComparingShit(numpy.asarray(original), numpy.asarray(comparing))
                m, s = good_fucking_class.compare_images
                s = int(round(s))
                if message.author.id == userID:
                    if s == percent:
                        return
                else:
                    UserID(message.author.id)
                    percentNew(s)
                if s >= 95:
                    break

        if s >= 90:
            try:
                await message.delete()
            except:
                pass

            await message.channel.send(f"{message.author.mention} Don't post that, It's lame [Warning].")
            return


def setup(bot):
    bot.add_cog(spritzalame(bot))