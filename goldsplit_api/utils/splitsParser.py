import xml.etree.ElementTree as ET

from rest_framework.exceptions import ParseError
from datetime import datetime
from statistics import mean

from .timeUtils import timeToMs



def parseSplits(file):
    #parses uploaded splits file
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        formattedSplits = []
        total_time = gold_total_time = 0

        for elem in root.iter('Segments'):
            segments = elem.findall('Segment')
            for split in segments:
                #from each split we need name, pb time, gold time, average time
                name = split.find('Name').text

                time = timeToMs(split.find('SplitTimes/SplitTime/RealTime').text)
                total_time += time

                gold_time = timeToMs(split.find('BestSegmentTime/RealTime').text)
                gold_total_time += gold_time

                #keep track of all segment times to get average
                seg_times = []
                for seg in split.findall('SegmentHistory/Time/RealTime'):
                    seg_times.append(timeToMs(seg.text))

                formattedSplits.append(
                    {
                        'name': name,
                        'time': time,
                        'total_time': total_time,
                        'gold_time': gold_time,
                        'gold_total_time': gold_total_time,
                        'average_time': round(mean(seg_times))
                    }
                )
            
        splits_info = {
            'game_name': root.find('./GameName').text,
            'category': root.find('./CategoryName').text,
            'splits': formattedSplits
        }

        return splits_info
                
    except:
        raise ParseError()