var KeyRow = function (rowData) {
    this.rowData = rowData;
    this.getRow = function () {
        return [
            rowData[0],
            rowData[1],
            rowData[2],
            this.getColorCls(rowData[3]),
        ]
    }
    this.getColorCls = function (cls) {
        return clsColorMap[cls].img + '<span style="font-weight: bold;color: ' + clsColorMap[cls].color + '">' + cls + '</span>'
    }
};

var clsColorMap = {
    "猎人Hunter": {
        color: "#ABD473",
        img: '<div class="GameIcon GameIcon--HUNTER GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "圣骑士Paladin": {
        color: "#F58CBA",
        img: '<div class="GameIcon GameIcon--PALADIN GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "德鲁伊Druid": {
        color: "#FF7D0A",
        img: '<div class="GameIcon GameIcon--DRUID GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "战士Warior": {
        color: "#C79C6E",
        img: '<div class="GameIcon GameIcon--WARRIOR GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "法师Mage": {
        color: "#69CCF0",
        img: '<div class="GameIcon GameIcon--MAGE GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "牧师Priest": {
        color: "#e5e5e5",
        img: '<div class="GameIcon GameIcon--PRIEST GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },//FFFFFF
    "死亡骑士Death Knight": {
        color: "#C41F3B",
        img: '<div class="GameIcon GameIcon--DEATHKNIGHT GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "术士Warlock": {
        color: "#9482C9",
        img: '<div class="GameIcon GameIcon--WARLOCK GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "潜行者Rogue": {
        color: "#FFF569",
        img: '<div class="GameIcon GameIcon--ROGUE GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "萨满祭司Shaman": {
        color: "#0070DE",
        img: '<div class="GameIcon GameIcon--SHAMAN GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "武僧Monk": {
        color: "#00FF96",
        img: '<div class="GameIcon GameIcon--MONK GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
    "恶魔猎手Demon Hunter": {
        color: "#A330C9",
        img: '<div class="GameIcon GameIcon--DEMONHUNTER GameIcon--vector GameIcon--tiny TalentCalculator-classIcon"><div class="GameIcon-icon"></div><div class="GameIcon-transmog"></div><div class="GameIcon-borderImage"></div></div>'
    },
};