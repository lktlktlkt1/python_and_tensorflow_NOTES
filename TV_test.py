from TV_class import TV
import random
def main():
    tv1=TV()
    tv1.turnOn()
    tv1.setChannel(5)
    tv1.setVolume(5)

    tv2=TV()
    tv2.turnOn()
    tv2.setChannel(5)
    tv1.setVolume(5)

    print(f"tv1's channel is {tv1.getChannel} and the volume level is {tv1.getvolumeLevel}")
    print(f"tv2's channel is {tv2.getChannel} and the volume level is {tv2.getvolumeLevel}")

main()
