import io
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from typing import List, Tuple
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt


def text_format_report(report: List[Tuple[datetime, int]]):
    formatted = '\n'.join(time.strftime('%H:%M:%S.%f') + ' ' + str(measurement) for time, measurement in report)
    return formatted


def chart_format_report(report: List[Tuple[datetime, int]]):
    time = [time for time, _ in report]
    load = [load for _, load in report]
    f = plt.figure()
    plt.plot(time, load, color='Blue')
    plt.xlabel('Time')
    plt.ylabel('CPU % Load')
    plt.title('CPU Load over time')
    binary = io.BytesIO()
    f.savefig(binary, bbox_inches='tight')
    binary.seek(0)
    email = MIMEMultipart()
    part = MIMEBase('application', 'octate-stream')
    # todo fix encoding
    part.set_payload(binary.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % 'report.pdf')
    email.attach(part)
    return email
