# Projects
Place for me to add projects that I haven't fully committed to for whatever reason.  
If you are interested in helping me with any of these projects please [contact me](https://kaisaan.github.io/pages/contact)  
I apologize for the awful notes files.

# Ys Book I & II (PCE-CD) Relocalization
**Info**: Not sure if "relocalization" is the right term but I want to edit the existing localization of the game to use the modern terms used in later *Ys* localizations and releases. Having Dogi be renamed as Colin is funny though  
**Progress**: Made a [table file](https://github.com/Kaisaan/projects/blob/main/ysbooks_table.tbl) and found the text, I don't think dumping text is needed. I also made a spreadsheet to compare what needs to be changed  
**Notes**: See [notes file](https://github.com/Kaisaan/projects/blob/main/ysbooks_notes.txt) and [localization changes spreadsheet](https://docs.google.com/spreadsheets/d/14efc2_Ah8uxgdXu9EfgDKUMMqBqisJnxj0-aCOOkT8I/edit?usp=sharing)  
**Status**: I'll work on this eventually I think. I know that the English localization of the game also had many [balance changes](https://tcrf.net/Ys:_Book_I_%26_II) but I haven't found the stats in the game's files yet

# Legacy of Ys - Books I & II (NDS) Relocalization
**Info**: Same thing like the PC-Engine version of the games, I wanted to fix Atlus' localization of the game to match the newer terms used.  
**Progress**: Text found but not editted yet  
**Notes**: The text for *Ys I* is in `overlay/main_0001.bin` and *Ys II* in `overlay/main_0002.bin` with the text using Shift-JIS encoding.  
I have columns in the [localization changes spreadsheet](https://docs.google.com/spreadsheets/d/14efc2_Ah8uxgdXu9EfgDKUMMqBqisJnxj0-aCOOkT8I/edit?usp=sharing) for this game too  
**Status**: The data area with all the text is a lot tighter in space, so I'll have to look for the text pointers before changing the text

# Rockman EXE N1 Battle (WSC) Translation
**Info**: Localized as *Mega Man Battle Chip Challenge N1*, this game is different from its GBA counterpart *Mega Man Battle Chip Challenge* being a cutdown version of it.  
**Progress**: Made an unfinished [table file](https://github.com/Kaisaan/projects/blob/main/mmnb_table.tbl) (thanks to Sugunii for the help!), found where the text is located  
**Notes**: See [notes file](https://github.com/Kaisaan/projects/blob/main/mmnb_notes.txt)  
**Status**: I don't have a full table file so I won't be able to dump all the text I think. I might just compare strings from the Japanese GBA version and then replace them with their English counterparts.

# Neon Genesis Evangelion (N64) Translation
**Info**: I have beat this game in full once thanks to the [multiple guides on GameFAQs](https://gamefaqs.gamespot.com/n64/198127-neon-genesis-evangelion/faqs) but I still want to have this game translated, especially since there are many other translated *Evangelion* games  
**Progress**: Zoinkitty has posted a file inserter and character font before on the [ROMhacking.net forums](https://web.archive.org/web/20201202192730/https://www.romhacking.net/forum/index.php?topic=22265.0) but the download links do not work any more.  
The filetable posted by Zoinkitty [is still available](https://web.archive.org/web/20170806110531/https://pastebin.com/Vt6SxCD3). Interestingly, a Korean translation of the game [did release](https://www.romhacking.net/translations/6260/) but by different people (and not OP)  
**Notes**: None from me  
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