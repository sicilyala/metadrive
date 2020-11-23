from pg_drive.envs.generalization_racing import GeneralizationRacing
from pg_drive.scene_creator.algorithm.BIG import BigGenerateMethod
import logging
from pg_drive.scene_manager.traffic_manager import TrafficMode
from pg_drive.utils import setup_logger

setup_logger(debug=True)


class ResetEnv(GeneralizationRacing):
    def __init__(self):
        super(ResetEnv, self).__init__(
            {
                "environment_num": 1,
                "traffic_density": 0.,
                "start_seed": 4,
                "debug": False,
                "bt_world_config": {
                    "force_fps": 40,
                    "debug_physics_world": False
                },
                "traffic_mode": TrafficMode.Reborn,
                "manual_control": True,
                "use_render": True,
                "use_rgb": False,
                "use_increment_steering": False,
                "map_config": {
                    "type": BigGenerateMethod.BLOCK_NUM,
                    "config": 7,
                },
                "vehicle_config": {
                    "front_cam": (200, 200)
                }
            }
        )
        self.reset()
        self.bullet_world.accept("r", self.reset)
        # self.bullet_world.cam.setPos(0, 0, 1500)
        # self.bullet_world.cam.lookAt(0, 0, 0)


if __name__ == "__main__":
    env = ResetEnv()
    import time

    env.reset()
    for i in range(1, 100000):
        # start = time.time()
        # print("Step: ", i)
        o, r, d, info = env.step([0.1, 0])
        # print(time.time() - start)
        # print(len(o), "Vs.", env.observation_space.shape[0])
        # print(info)
        env.render(text={"can you see me": i})
        # if d:
        #     print("Reset")
        #     env.reset()
    env.close()
