from datetime import timedelta

from cpu_reporter.email_sender import chart_send_mail
from cpu_reporter.formatter import chart_format_report
from cpu_reporter.report_generator import generate_report


class CpuReporter:
    def __init__(self, generator, formatter, sender):
        self.__sender = sender
        self.__formatter = formatter
        self.__generator = generator

    def send_report(self):
        # SRP
        # todo downsampling for longer periods
        report = self.__generator(duration=timedelta(seconds=2))
        formatted = self.__formatter(report)
        self.__sender(formatted)


def main():
    # plain_text_reporter = CpuReporter(generate_report, text_format_report, text_send_email)
    # plain_text_reporter.send_report()
    chart_reporter = CpuReporter(generate_report, chart_format_report, chart_send_mail)
    chart_reporter.send_report()


if __name__ == '__main__':
    # inversion of controll
    main()
