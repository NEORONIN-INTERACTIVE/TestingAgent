"""
Competition agent template - rename this package and customize!
"""

from w4a import CompetitionAgent


class TestingAgent(CompetitionAgent):
    """
    Your competition agent. Inherit from CompetitionAgent and override select_action().
    
    Rename this class and package to something unique (e.g., TeamAlphaAgent).
    """
    
    def __init__(self, faction, config):
        super().__init__(faction, config)
        # Initialize your agent here (e.g., load a trained model)
        self.log("Agent initialized")
    
    def log(self, message):
        """Print a log message with faction prefix."""
        print(f"[{self.faction.name}] {message}")
    
    def select_action(self, observation):
        """
        Choose an action based on the current observation.
        
        Args:
            observation: Game state as numpy array (see docs/OBSERVATION_SPACE.md)
            
        Returns:
            Action dict (see docs/ACTION_SPACE.md)
        
        Available helper methods (see w4a/agents/competition_agent.py for full API):
            self.get_alive_entities()        - Your alive controllable units
            self.get_all_entities()          - All your units (alive and dead)
            self.get_target_groups()         - Detected enemy groups
            self.get_entity_by_id(id)        - Get specific entity by ID
            self.get_target_group_by_id(id)  - Get specific target group by ID
            self.get_capture_capable_entities() - Units that can capture flags
            self.get_refuelable_entities()   - Units that can receive fuel
            self.is_entity_capturing(id)     - Check if unit is capturing a flag
            self.is_entity_refueling(id)     - Check if unit is refueling
        """
        # Example: log state each step
        # entities = self.get_alive_entities()
        # enemies = self.get_target_groups()
        # self.log(f"Entities: {len(entities)}, Enemies detected: {len(enemies)}")
        
        # TODO: Replace with your policy
        return self.action_space.sample()
