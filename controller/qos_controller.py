from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4

class QoSController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(
            ofproto.OFPIT_APPLY_ACTIONS, actions)]

        flow = parser.OFPFlowMod(
            datapath=datapath,
            priority=priority,
            match=match,
            instructions=inst)

        datapath.send_msg(flow)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto

        # Default flow (LOWEST PRIORITY)
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL)]
        self.add_flow(datapath, 0, match, actions)

        print("Default flow installed")

        # HIGH PRIORITY: h1
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src='10.0.0.1'
        )
        self.add_flow(datapath, 300, match, actions)
        print("High priority flow for h1")

        # MEDIUM PRIORITY: h2
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src='10.0.0.2'
        )
        self.add_flow(datapath, 200, match, actions)
        print("Medium priority flow for h2")

        # LOW PRIORITY: h3
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src='10.0.0.3'
        )
        self.add_flow(datapath, 100, match, actions)
        print("Low priority flow for h3")
