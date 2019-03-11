import unittest
from api.utils.packet_builder import PacketBuilder
from api.utils.packet import Packet

class TestPacketBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.builder = PacketBuilder('localhost', 5555)

    def testAddCommand(self):
        self.builder.addCommand('get')
        self.assertEqual(self.builder.cmd, 'get')

    def testAddArgument(self):
        self.builder.addArgument('base')
        self.assertEqual(self.builder.args, ['base'])
    
    def testAddArguments(self):
        self.builder.addArguments('base', 'top')
        self.assertEqual(self.builder.args, ['base', 'top'])

    def testAddParameter(self):
        self.builder.addParameter('play')
        self.builder.addParameter('-pause')
        self.builder.addParameter('--stop')
        self.assertEqual(self.builder.params, ['--play', '--pause', '--stop'])

    def testAddParameters(self):
        self.builder.addParameters('play', '-pause', '--stop')
        self.assertEqual(self.builder.params, ['--play', '--pause', '--stop'])

    def testAddKeyValuePair(self):
        self.builder.addKeyValuePair('speed', '5')
        self.assertDictEqual(self.builder.keys, {'speed': '5'})

    def testBuild(self):
        packet = self.builder.addCommand('get').addParameter('help').build()
        self.assertEqual(packet, Packet('localhost', 5555, 'cmd/json/get?--help'))

if __name__ == '__main__':
    unittest.main()