# Python bytecode 3.7 (3394)
# Embedded file name: C:\Users\joelt\Desktop\AkaneBot\cogs\autoban.py
# Size of source mod 2**32: 6760 bytes
# Decompiled by https://python-decompiler.com (uncompyle6 threw up errors when trying to decompile this one)
import asyncio, aiohttp, discord
from discord.ext import commands
from discord.ext.commands import BucketType
import subprocess, numpy, os, pathlib, requests, re, shutil, time
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


class autoban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    def on_message(self, ban):
        if ban.author.bot:
            return
        guild = self.bot.get_guild(615881983310036992)
        channel = guild.get_channel(699601874671763477)
        if ban.content.startswith('.badimage'):
            return
        try:
            await ban.attachments[0].save('bad/image.jpg')
        except:
            return
        else:
            before = time.monotonic()
            for file in os.listdir('badlist'):
                original = Image.open(f"badlist/{file}").convert('L')
                w, h = original.size
                try:
                    comparing = Image.open('bad/image.jpg').convert('L').resize((w, h))
                except Image.DecompressionBombError:
                    return
                except:
                    return

                good_fucking_class = ComparingShit(numpy.asarray(original), numpy.asarray(comparing))
                m, s = good_fucking_class.compare_images
                s = int(round(s))
                if s >= 90:
                    fuck = 'bad/image.jpg'
                    you = 'confirmbad/image.jpg'
                    shutil.copyfile(fuck, you)
                    break

            timer = (time.monotonic() - before) * 1000
            files = discord.File('confirmbad/image.jpg', filename='SPOILER_image.jpg')
        if s >= 90:
            try:
                pass
            except:
                pass

            await channel.send(f"I am {s}% positive **{ban.author.name}**#{ban.author.discriminator} ({ban.author.id}) posted a troll file in <#{ban.channel.id}>.\nThe user would be banned.", file=files)
            await channel.send(f"It took {int(timer)}ms to calculate this image *(Not including how long it took to upload)*")
            return
        if s >= 75:
            try:
                await ban.delete()
                await channel.send(f"I am {s}% positive **{ban.author.name}**#{ban.author.discriminator} ({ban.author.id}) posted a troll file in <#{ban.channel.id}>.\nThe message was deleted.", file=files)
            except:
                await channel.send(f"I am {s}% positive **{ban.author.name}**#{ban.author.discriminator} ({ban.author.id}) posted a troll file in <#{ban.channel.id}>.\nThe message isn't deleted.", file=files)

            return

    @commands.command()
    def badimage(self, ctx, *, imagename=None):
        if not ctx.author.guild_permissions.manage_messages:
            return
        if imagename is None:
            await ctx.send('Please give the image a name to save it as.', delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
        if pathlib.Path(f"badlist/{imagename}.png").is_file():
            await ctx.send('Image name already exist. Please give it another name.')
            return
        try:
            await ctx.message.attachments[0].save(f"badlist/{imagename}.png")
            await ctx.send('Image saved.', delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
        except:
            await ctx.send('No image provided or an issue occured.')

    @commands.command()
    def removeimage(self, ctx, *, imagename=None):
        if not ctx.author.guild_permissions.manage_messages:
            return
        if imagename is None:
            await ctx.send('Please give the image name to remove.')
            return
        if pathlib.Path(f"badlist/{imagename}").is_file():
            os.remove(f"badlist/{imagename}")
            await ctx.send('Image was sucessfully deleted')
            return
        await ctx.send('Image does not exist.')

    @commands.command()
    def viewimage(self, ctx, *, imagename=None):
        if not ctx.author.guild_permissions.manage_messages:
            return
        if imagename is None:
            files = os.listdir('badlist')
            files1 = ', '.join(files)
            files1 = files1.replace(', ', '\n')
            await ctx.send(f"Valid images:\n{files1}")
        elif pathlib.Path(f"badlist/{imagename}").is_file():
            f = discord.File(f"badlist/{imagename}", filename=f"SPOILER_{imagename}.gif")
            await ctx.send('Image will be delete after 15 seconds', file=f, delete_after=15)
            await asyncio.sleep(15)
            await ctx.message.delete()
        else:
            await ctx.send('Image does not exist.')


def setup(bot):
    bot.add_cog(autoban(bot))