import socket
import sys
from typing import List
from argparse import ArgumentParser
from chroma_feedback import helper, wording
from chroma_feedback.typing import Status, Consumer
from .light import get_lights, process_lights

ARGS = None


def support() -> bool:
	return helper.is_linux() is True or helper.is_mac() is True or helper.is_windows() is True


def init(program : ArgumentParser) -> None:
	global ARGS

	if not ARGS:
		ips = None

		if not helper.has_argument('--nanoleaf-light-ip'):
			ips = discover_ips()
		if ips:
			program.add_argument('--nanoleaf-light-ip', default = ips)
		else:
			program.add_argument('--nanoleaf-light-ip', action = 'append', required = True)
	ARGS = helper.get_first(program.parse_known_args())


def run(status : Status) -> List[Consumer]:
	lights = get_lights(ARGS.nanoleaf_light_ip)

	if not lights:
		sys.exit(wording.get('light_not_found') + wording.get('exclamation_mark'))
	return process_lights(lights, status)


def discover_ips() -> List[str]:
	ips = []
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'MAN: "ssdp:discover"',
		'ST: nanoleaf:nl29'
	]
	discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	discovery.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	discovery.settimeout(2)
	discovery.sendto('\r\n'.join(message).encode(), ('239.255.255.250', 1900))

	try:
		ips.append(helper.get_first(discovery.recvfrom(65507)[1]))
	except OSError:
		sys.exit(wording.get('ip_not_found').format('NANOLEAF LIGHT') + wording.get('exclamation_mark'))
	return ips
