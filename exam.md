CH-01 計算機抽象化與科技
抽象化 (Abstraction): 隱藏實作細節，只留下語意結構

ISA: instruction set architecture，提供軟體和硬體的語意介面

摩爾定律 (Moore's Law): 描述IC上的電晶體密度每**18~24個月**就會翻倍，大致描述硬體界的成長速度

記憶體階層 (Hierarchy of Memories): **一種利用多個不同成本、速度和容量，來提供接近頂層速度，接近底層成本與容量的儲存系統。**

CPU 效能方程式 (CPU Performance Equation): 描述CPU的效能，CPUtime = instructions * CPI * Ghz

CPI: cycles per instruction，描述CPU的一個ISA指令要執行多少個clock

功耗障壁 (The Power Wall): 電進得去，熱出的來，台灣發大財。描述IC的設計難題(熱與電)，如果電壓太低會導致漏電，頻率太高會導致過熱

Amdahl's 定律 (Amdahl's Law): 計算效能提升幅度的定律，說明效能得整體提升局限於系統中未受改善的部分。

CH-02 指令：計算機的語言
內儲程式的觀念 (Stored-Program Concept): 程式和資料不分開儲存，統一以數字儲存在記憶體裡

2的補數 (Two's Complement): 使數字不需要額外硬體即能在加法機上同時做加減法的數字表示方式

符號延伸 (Sign Extension): 將signed從少位元延伸到較多位元，同時保持數值和符號不變的過程。

對齊限制 (Alignment Restriction): 要求N byte的資料必須儲存在N倍的記憶體位置上。

Endianness (位元組排序): 對於不能儲存在一個byte裡的資料，規定byte的大小排序方式，分為big endian何little endian

虛擬指令 (Pseudoinstruction): 抽象化的指令，硬體上實際並沒有這個指令，而是透過組譯器翻譯來實現(如move -> add)

PC 相對定址法 (PC-Relative Addressing): 透過PC+address來跳到指定位置的方式

堆疊 (Stack): 一種LIFO結構，在程序呼叫時保存暫存器。

載入一聯結 / 條件儲存 (ll / sc): ____________________

聯結器 (Linker): 一個系統程式，負責將各自組譯好的目標檔縫合成一個可執行檔。

CH-03 計算機算術
ALU (Arithmetic Logic Unit): CPU裡實際在進行運算的地方，進行算數(如add sub)和邏輯運算(如or xor)

溢位 (Overflow): 數字超出了硬體bit所能表示的範圍

漣波進位加法器 (Ripple Carry Adder): 每一個bit的cin皆為前一個bit的cout來計算

前瞻進位加法器 (Carry Look-ahead Adder, CLA): 藉由空間換取時間的加法機實現方式，每一個bit的carry皆與前面所有bit相關

布斯演算法 (Booth's Algorithm): 一種計算signed數字的乘法的方式

浮點數 (Floating Point): 電腦裡藉由科學記號儲存實數的方法，由signed,exponent,significand組成，用以在有限維園內表示非常大或非常小的數。

IEEE 754: 規定浮點數格式的一個格式

偏移表示法 (Biased Notation): 借由數字+bias來表示數字的方法，如float中的excess

NaN (Not a Number): 非數職的縮寫，一種特殊的浮點數值，用瑜表示無效或為定義的運算結果。

非正規化數 (Denormalized Number): 一種特殊的值非常小的浮點數表示法