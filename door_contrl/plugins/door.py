from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import USER
import random
import httpx
from nonebot.adapters.cqhttp.permission import GROUP_ADMIN

door = on_command("开门",   priority=5, permission=GROUP_ADMIN, aliases={"km"})


@door.handle()
async def handle_city(bot: Bot, event: Event, state: T_State):
        async with httpx.AsyncClient() as client:
            await client.get("http://18.gs.cn:18000/Index/Door/door_open?token=1639356123", timeout=1000)

        message_All = ["没有谁的生活会一直完美，满怀希望就会所向披靡\n欢迎回家~", "世界灿烂盛大，欢迎回家\n欢迎回家~", "白雾奔涌，天使归乡\n欢迎回家~", "看过世界的人，最想回家\n欢迎回家~",
                       "一日不见，如三秋兮\n欢迎回家~", "山气日夕佳，飞鸟相与还\n欢迎回家~", "羁鸟恋旧林，池鱼思故渊\n欢迎回家~", "长风破浪会有时，直挂云帆济沧海\n欢迎回家~"]
        await door.finish(message=message_All[random.randint(0, 7)])
