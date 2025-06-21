# Projects
Place for me to add projects that I haven't fully committed to for whatever reason.  
If you are interested in helping me with any of these projects please [contact me](https://kaisaan.github.io/pages/contact).  
Feel free to join [my Hacking Discord server](https://discord.gg/JnqvyDryen) where I plan on posting updates for all my projects.  
I apologize for the awful notes.

# Ys Book I & II (PCE-CD) Relocalization
**Info**: Not sure if "relocalization" is the right term but I want to edit the existing localization of the game to use the modern terms used in later *Ys* localizations and releases. Having Dogi be renamed as Colin is funny though  
**Progress**: Made a [table file](https://github.com/Kaisaan/projects/blob/main/ysbooks_table.tbl) and found the text, I don't think dumping text is needed. I also made a spreadsheet to compare what needs to be changed  
**Notes**: See [notes file](https://github.com/Kaisaan/projects/blob/main/ysbooks_notes.txt) and [localization changes spreadsheet](https://docs.google.com/spreadsheets/d/14efc2_Ah8uxgdXu9EfgDKUMMqBqisJnxj0-aCOOkT8I/edit?usp=sharing)  
**Status**: I'll work on this eventually I think. I know that the English localization of the game also had many [balance changes](https://tcrf.net/Ys:_Book_I_%26_II) but I haven't found the stats in the game's files yet

# Legacy of Ys - Books I & II (NDS) Relocalization
**Info**: Same thing like the PC-Engine version of the games, I wanted to fix Atlus' localization of the game to match the newer terms used.  
**Progress**: Some of the text has been edited.  
**Notes**: The text for *Ys I* is in `overlay/main_0001.bin` and *Ys II* in `overlay/main_0002.bin` with the text using Shift-JIS encoding. All overlays are loaded at `0x205C000`. Names of locations on the map are in different `.inf` files located in `data\ys1\files\inf`.    
I have columns in the [localization changes spreadsheet](https://docs.google.com/spreadsheets/d/14efc2_Ah8uxgdXu9EfgDKUMMqBqisJnxj0-aCOOkT8I/edit?usp=sharing) for this game too.  
**Status**: I figured out how to load NDS projects into Ghidra, some strings don't seem to have pointers but that should be fine. I will start working on it more.

# Rockman EXE N1 Battle (WSC) Translation
**Info**: Localized as *Mega Man Battle Chip Challenge N1*, this game is different from its GBA counterpart *Mega Man Battle Chip Challenge* being a cutdown version of it.  
**Progress**: Made an unfinished [table file](https://github.com/Kaisaan/projects/blob/main/mmnb_table.tbl) (thanks to Sugunii for the help!), found where the text is located.  
**Notes**: See [notes file](https://github.com/Kaisaan/projects/blob/main/mmnb_notes.txt)  
**Status**: I don't have a full table file so I won't be able to dump all the text I think. I might just compare strings from the Japanese GBA version and then replace them with their English counterparts.

# Ys Remakes (PS2) Translations
**Info**: While I already have been working on translating [*Ys V: Lost Kefin, Kingdom of Sand*](https://github.com/Kaisaan/lostkefin) as one of my main projects, I eventually want to translate the other *Ys* games that were remake on the PS2.  
**Progress**: I only looked at the file structures for all of the games' ISOs.  
**Notes**: The only different between the normal and the "Tokubetsu Genteiban" releases of *Ys I & II - Eternal Story* is a single byte change (in `SYSTEM.CNF` to change `SLPS_252.06` to `SLPS_252.05`).  
*Ys III - Wanderers from Ys* has the extact same file structure as *Ys V* by having `DATA.BIN`, `DATA0.BIN`, and `DATA1.BIN` for all the game's data. This should be the easiest to hack next.  
*Ys IV - Mask of the Sun, A New Theory* has `DAT.PAK` and `DAT.PKI` to store all its gamedata.  
**Status**: I can't really do anything right now with these games since I don't have any translators. If there is anything worth changing, Please contact me if you want to help!

# Shin Megami Tensei Devil Children: Black Book (GBC) Translation
**Info**: While [there already is a translation](https://www.romhacking.net/translations/6163/) for the game, the translation quality was critisized. I managed to find an old, full translated script of the game done by Translator Tom. I asked for permission to use the script as a personal project.  
**Progress**: I was able to get most of the Japanese script dumped and inserted the first few lines of the game.  
I got in contact with [Specialagentape](https://www.romhacking.net/community/5916/), the hacker and editor of the original project. They explained to me that most of the script that their translator [Higsby](https://www.romhacking.net/community/2697/) worked on had to be trimmed down a lot due to the limitted space that the Gameboy (Colour) screen has. This is completely understandable on their end.  
I also got in contact with Tom for permission to use their old English translation. They wanted me to not release anything if I do use their script, but if I ever finished up anything, they would be willing to make a new translated script.  
So ideally, I'd have to implement some methods to increase the number of possible letters on a screen, such as implementing a Variable Width Font (VWF) routine.    
**Notes**: I used the [ROMhacking tutorials by Bunkai](https://www.romhacking.net/community/7232/) to help with hacking the game. My files for this project were a complete mess.  
**Status**: I might return to this one day and also try hacking the counterpart game *Red Book* or its sequel game *White Book*. Hopefully we see more *Devil Children* translations in general since there's still a good few games left untranslated.

# Digitial Devil Story: Megami Tensei (PC-88) Translation
**Info**: After I successfully made a full translation of [the MSX version of the game](https://www.romhacking.net/translations/7180/) I wanted to try translating the other versions since the MSX release is distinct from the others. Since I had already beat the PC-88 version I wanted to try translating that.  
**Progress**: With the help of MKCA, we were able to make a full table file for all the characters used in the PC-88 BIOS files, including the Kanji tables. The text for the game was found and I was able to edit it. The issue is that there is a lack of space available to add longer text or even use non-fullwidth characters.  
**Notes**: None
**Status**: If I can get better at hacking Japanese PCs like the PC-88, or even the Sharp X1 and FM-7, I can translate the game. It's a shame that there isn't that many resources for hacking these systems.

# Popful Mail (PCE-CD) Tranlsation
**Info**: Popful Mail is one of the more underrated titles by Nihon Falcom. There are multiple versions released but the only one that was officially localized (though poorly translated) was the Sega CD version. The PCE-CD version of the game is also popular and recently Forrealsyall made a full [translated playthough](https://www.youtube.com/playlist?list=PLj4ote4X6Yf5svx1ZDcXNomVAGbjJB7NJ) of the game. Which made me interested in trying to hack it to insert their translation. Big thanks to [X-pert74](https://bsky.app/profile/x-pert74.bsky.social) for bringing this to my attention!    
**Progress**: I found the game's text and managed to edit it. But the font is very large it would be ideal to support ASCII encoding.
**Notes**: Game uses Shift-JIS encoding.  
**Status**: I'm technically actively working on this. I will need to look more into this.

# Wild Arms: Alter Code F (PS2) Relocalization
**Info**: The only *Wild Arms* game I've played is the first *Wild Arms* but I'm interested in playing the other games too, including its remake on the PS2. Thanks to [Lime](https://bsky.app/profile/limetimebaby.bsky.social) for letting me know that the game's script could use a better translation, or at least be editted to sound better. The original Japanese release also had voices for the characters in battles that were removed in the English localization so I want to try to restore those voices.  
**Progress**: I found the game's text and the game still seems to have the voice files, I just need to find a way to make them play in-game.  
**Notes**: Game uses Shift-JIS encoding(?) for its text. Many files are idential between USA and JAP releases.  
**Status**: I'm still working on this.  

# Neon Genesis Evangelion (N64) Translation
**Info**: I have beat this game in full once thanks to the [multiple guides on GameFAQs](https://gamefaqs.gamespot.com/n64/198127-neon-genesis-evangelion/faqs) but I still want to have this game translated, especially since there are many other translated *Evangelion* games  
**Progress**: Zoinkitty has posted a file inserter and character font before on the [ROMhacking.net forums](https://web.archive.org/web/20201202192730/https://www.romhacking.net/forum/index.php?topic=22265.0) but the download links do not work any more.  
The filetable posted by Zoinkitty [is still available](https://web.archive.org/web/20170806110531/https://pastebin.com/Vt6SxCD3). Interestingly, a Korean translation of the game [did release](https://www.romhacking.net/translations/6260/) but by different people (and not OP)  
**Notes**: None from me.  
**Status**: I might return to this eventually, but hopefully an N64 hacking expert like Zoinkitty tackles this instead

# Gekisou Sentai Carranger: Zenkai! Racer Senshi (SFC) Translation
**Info**: I only know about this game because of the music track [*Select Your Carranger!](https://www.youtube.com/watch?v=8AS-8wsledg) but still I want to try translating this game eventually  
**Progress**: I haven't found any of the text graphics or text itself  
**Notes**: None  
**Status**: I will need to learn more about 65c816 assembly to hack this game

# Ys I: Ancient Ys Vanished (PC-88) Translation
**Info**: I think by now you can tell that I really like Ys, so I wanted to see what I could get translation hacks going for.  
**Progress**: I made a pretty basic table file based off of the PC-88 BIOS files and also found the text for the game  
**Notes**: Nothing to say here  
**Status**: **Cancelled**, well, only *my* version of the translation project. I found someone that is working on translating the entire PC-88 *Ys* trilogy, so there's no reason for me to continue working on this (they've made much more progress). I'll update this whenever that project is finished

# Erst Kerf (PC) Translation
**Info**: A really cool shump/dungeon crawler doujin game with a really cool artstyle and soundtrack that I saw my friend Sugunii play. The game seems to have a story but is sadly untranslated so I decided to look into if I could find the text.  
**Progress**: I found the text but I have no translator.  
**Notes**: Text for the game can be found in the `date` folder in the indiviual `.scp` files for each stage. The stages' script files seem to just have a `text ""` command which can be changed.  
**Status**: This is just something I looked into for curiousity. If someone is interested in translating the game it seems pretty simple to do so.

# Witch's Wish (NDS) Sprite Extraction
**Info**: A game I don't really know much about but my friend wanted to get the sprites extracted as regular image files.  
**Progress**: After unpacking the ROM with [NitroPacker](https://github.com/haroohie-club/NitroPacker) I was able to find the characters' graphics in `data/2d/cast` as file formats that were recognized by [NitroPaint](https://github.com/Garhoogin/NitroPaint) and was able to extract.  
**Notes**: None  
**Status**: I guess this is considered complete? Once NitroPaint has the function to export NANR animations as .GIF files, extracting the character animations would be faster.

# A Witch's Tale (NDS) Script Extraction
**Info**: Same thing with *Witch's Wish* my friend wanted to extract the graphics of the game because they love the cute artstyle.  
**Progress**: I couldn't do much, the game has a lot of overlays and a single `romfile.bin` so I'd have to do some more manual work to extract the sprites.  
**Notes**: None
**Status**: Even though I didn't get much done I still wanted to add it here so I can get into the habit of posting about future tinkering with other games.