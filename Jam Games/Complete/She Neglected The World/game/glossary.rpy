define config.hyperlink_protocol = "showmenu"

# -------------------------------------------------------------------------------------------------
screen glossary_cultivation():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Cultivation"

        text _p("""

The practice of refining the mind, body, and spirit onto the path of immortality and or enlightenment. Those who cultivate are referred to as cultivators.

This world has 7 stages of cultivation as follows:

Qi Condensation{p}
Foundation Establishment{p}
Core Formation{p}
Nascent Soul{p}
Soul Formation{p}
Soul Transformation{p}
Ascendant{p}

After the Ascendant stage, a cultivator reaches the goal of true immortality and ascends to the Heavens.

Those who cultivate an evil path using demonic energy are referred to as demonic cultivators.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)


screen glossary_fairy():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Fairy"

        text _p("""

Not to be confused with western fairies or fae. Fairy is a term used to refer to beautiful women, typically cultivators

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_heavenly_way():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Heavenly Way"

        text _p("""

Also known as the Will of Heaven. It is a just force that commands the fate of the realms, sends tribulations as trials to those who dare seek immortality, maintains vows made to it, and punishes evildoers.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)


screen glossary_array():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Array"

        text _p("""

Spell formations typically drawn like a magic circle, often with an area of effect result.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_heart_demon():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Heart Demon"

        text _p("""

Negative emotions or mental barriers that hinder a cultivator's training, becoming dangerous obsessions. They may attack the cultivator from within and result in {a=glossary_qi_deviation}Qi Deviation{/a}.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_qi_deviation():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Qi Deviation"

        text _p("""

A physiological or psychological disorder caused by improper practice of {a=glossary_cultivation}Cultivation{/a}.{p}A cultivator's spiritual energy may go out of control, destroying the mind and body.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_closed_door_cultivation():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Closed Door Cultivation"

        text _p("""

Cultivation training done in seclusion, often at crucial moments in a cultivator's {a=glossary_cultivation}Cultivation{/a}.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_fenghuang():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Fenghuang"

        text _p("""

A mythological bird with superficial similarities to the western phoenix.{p}
They are symbols of the royal family and the union of yin-yang, the blissful relationship between husband and wife. Feng refers to the males of the species while huang refers to the females of the species.{p}Depending on the era, both genders may be amalgamated into one feminine fenghuang, which is paired with the dragon.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_yao():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Yao"

        text _p("""

An animal, plant, or inanimate object that has gained spiritual awareness after absorbing spiritual energy for a long time. They may take on the forms of monsters or even humans, but they are not inherently antagonistic to people.

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_idiom():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "White hairs of old age"

        text _p("""

The idiom {i}bai2 tou2 xie2 lao3{/i} refers to a married couple living to a ripe old age in conjugal bliss. Their white hairs represent the time they spent together from their youths when their hair was black till their last days when their hair has already turned white. The idiom is also interpreted as "until death do we part."{p}

{a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_zhuangzi():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Zhuangzi"

        text _p("""

A major philosophical text considered a foundational text of Taoism. Zhuangzi (Chuang Tzu) is a  collection of anecdotes, allegories, parables, and fables written in the Late Warring States period of China.

Among the most famous of the stories within the text are {a=glossary_the_butterfly_dream}The Butterfly Dream{/a} and {a=glossary_the_joy_of_fish}The Joy of Fish{/a}.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_the_joy_of_fish():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "The Joy of Fish"

        text _p("""

{a=glossary_zhuangzi}Zhuangzi{/a} and Huizi were crossing the Hao River by the dam.{p}
Zhuangzi said, "See how free the fishes leap and dart: that is their happiness."{p}
Huizi replied, "Since you are not a fish, how do you know what makes fishes happy?"{p}
Zhuangzi said, "Since you are not I, how can you possibly know that I do not know what makes fishes happy?"{p}
Huizi argued, "If I, not being you, cannot know what you know, it follows that you, not being a fish, cannot know what they know. The argument is complete!"{p}
Zhuangzi said, "Wait a minute! Let us get back to the original question. What you asked me was 'How do you know what makes fishes happy?' From the terms of your question, you evidently know I know what makes fishes happy."{p}
"I know the joy of fishes in the river through my own joy, as I go walking along the same river."{p}

Translation by Thomas Merton, The Way of Zhuang Tzu, New Directions Books, 1965

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_the_butterfly_dream():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "The Butterfly Dream"

        text _p("""

One night, {a=glossary_zhuangzi}Zhuangzi{/a} dreamed of being a butterfly — a happy butterfly, showing off and doing things as he pleased, unaware of being Zhuangzi. Suddenly he awoke, drowsily, Zhuangzi again. And he could not tell whether it was Zhuangzi who had dreamt the butterfly or the butterfly dreaming Zhuangzi. But there must be some difference between them! This is called 'the transformation of things'.{p}

{a=https://en.wikiquote.org/wiki/Zhuangzi}Zhuangzi (wikiquote){/a}{p}
{a=https://creativecommons.org/licenses/by-sa/3.0/ }Shared under Creative Commons Attribution-ShareAlike License{/a}{p}

The butterfly dream is referred to as {i}mengdie{/i}.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_bai_juyi():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Bai Juyi"

        text _p("""

A Tang dynasty government official and prolific poet. Many of his poems are observations about everyday life, but he also wrote a number of long narrative poems.

His works include {a=glossary_the_peach_blossoms_of_dalin_temple}The Peach Blossoms of Dalin Temple{/a} and {a=glossary_song_of_everlasting_sorrow}Song of Everlasting Sorrow{/a}.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_the_peach_blossoms_of_dalin_temple():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "The Peach Blossoms of Dalin Temple"

        text _p("""

A poem written by Tang dynasty poet {a=glossary_bai_juyi}Bai Juyi{/a} in the year 817.

In the human realm, April’s flowers are beginning to wither,{p}
But on this mountain, the temple’s peach blossoms are just starting to bloom.{p}
I always complained that spring flew by too quickly,{p}
Not knowing that spring only moved up here.{p}

Translation from: {a=https://frommetertomeaning.wordpress.com/%E5%A4%A7%E6%9E%97%E5%AF%BA%E6%A1%83%E8%8A%B1-%E7%99%BD%E5%B1%85%E6%98%93-the-peach-blossoms-of-dalin-temple-bai-juyi/}The Peach Blossoms of Dalin Temple{/a}

The "flowers" mentioned in the first line are written with the pair of Chinese characters read as {i}fangfei{/i}, a literary term referring to flowers and plants or the fragrance of flowers and plants.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

screen glossary_song_of_everlasting_sorrow():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Song of Everlasting Sorrow"

        text _p("""

A long narrative poem written by Tang dynasty poet {a=glossary_bai_juyi}Bai Juyi{/a} in year 806.

"The emperor neglected the world from that moment,{p}
Lavished his time on her in endless enjoyment.{p}
She was his springtime mistress, and his midnight tyrant.{p}
Though there were three thousand ladies all of great beauty,{p}
All his gifts were devoted to one person."{p}

(an excerpt of the poem as translated by A.S. Kline)\n\n{p}

The poem describes the tragic love of Emperor Xuanzong from a previous dynasty and his calamitous consort, Yang Guifei.\n{p}

The phrase {i}muqing{/i} is used in the original text in the line translated to "His majesty’s love remained, deeper than the new" by Kline to describe Emperor Xuanzong's yearning for his consort day and night.{p}

            {a=showmenu:glossary_index}Back to Index{/a}
            """)

# -------------------------------------------------------------------------------------------------

screen glossary_index():

    tag menu

    use game_menu(_("Glossary"), scroll="viewport", _extras=True):
      style_prefix "glossary"
      vbox:
        label "Glossary Index"

        vbox:
            text _p("""
                • {a=glossary_array}Array{/a}{p}
                • {a=glossary_bai_juyi}Bai Juyi{/a}{p}
                • {a=glossary_closed_door_cultivation}Closed Door Cultivation{/a}{p}
                • {a=glossary_cultivation}Cultivation{/a}{p}
                • {a=glossary_fairy}Fairy{/a}{p}
                • {a=glossary_fenghuang}Fenghuang{/a}{p}
                • {a=glossary_heart_demon}Heart Demon{/a}{p}
                • {a=glossary_heavenly_way}Heavenly Way{/a}{p}
                • {a=glossary_idiom}an idiom about white hairs of old age{/a}{p}
                • {a=glossary_qi_deviation}Qi Deviation{/a}{p}
                • {a=glossary_song_of_everlasting_sorrow}Song of Everlasting Sorrow{/a}{p}
                • {a=glossary_the_butterfly_dream}The Butterfly Dream{/a}{p}
                • {a=glossary_the_joy_of_fish}The Joy of Fish{/a}{p}
                • {a=glossary_the_peach_blossoms_of_dalin_temple}The Peach Blossoms of Dalin Temple{/a}{p}
                • {a=glossary_yao}Yao{/a}{p}
                • {a=glossary_zhuangzi}Zhuangzi{/a}{p}
            """)


style glossary_label is gui_label
style glossary_label_text is gui_label_text

style glossary_label_text:
    text_align 0.5
    layout "subtitle"
    color "#562827"
    outlines [ (absolute(2), "#ffffff", absolute(0), absolute(0)) ]
