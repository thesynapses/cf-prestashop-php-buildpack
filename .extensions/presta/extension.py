"""Prestashop Extension

Downloads, installs and configures Prestashop
"""
import os
import os.path
import logging
from build_pack_utils import utils


_log = logging.getLogger('prestashop')


DEFAULTS = utils.FormattedDict({
	'PRESTASHOP_VERSION': '1.6.0.9',  # or 'latest'
	'PRESTASHOP_PACKAGE': 'prestashop_{PRESTASHOP_VERSION}.zip',
	'PRESTASHOP_HASH': '0',
	'PRESTASHOP_URL': 'http://www.prestashop.com/download/old/{PRESTASHOP_PACKAGE}'
})


# Extension Methods
def preprocess_commands(ctx):
	return ()


def service_commands(ctx):
	return {}


def service_environment(ctx):
	return {}


def compile(install):
	print 'Installing Prestashop %s' % DEFAULTS['PRESTASHOP_VERSION']
	ctx = install.builder._ctx
	inst = install._installer
	workDir = os.path.join(ctx['TMPDIR'], 'prestashop')
	inst.install_binary_direct(
		DEFAULTS['PRESTASHOP_URL'],
		DEFAULTS['PRESTASHOP_HASH'],
		workDir,
		fileName=DEFAULTS['PRESTASHOP_PACKAGE'],
		extract=True)
	workDir = os.path.join(workDir, 'prestashop')
	(install.builder
		.move()
		.everything()
		.under('{BUILD_DIR}/htdocs')
		.into(workDir)
		.done())
	(install.builder
		.move()
		.everything()
		.under(workDir)
		.into('{BUILD_DIR}/htdocs')
		.done())
	return 0
