from backend import web
from trajectory_builder import TrajectoryBuilder
import threading
from agents.model import TrainingSystem


def main():
    env_lst = ['CartPole-v0', 'MountainCarContinuous-v0', 'Pendulum-v0', 'LunarLanderContinuous-v2']

    # create the trajectory builder
    trajectory_builder = TrajectoryBuilder()

    # start up the flask backend api
    app = web.get_webapp(trajectory_builder, env_lst)
    threading.Thread(target=app.run, args=['0.0.0.0', 5000]).start()

    training_system = TrainingSystem(env_lst[1])
    threading.Thread(target=training_system.pretrain_model(), args=[True]).start()
    threading.Thread(target=training_system.play, args=[True]).start()



if __name__ == "__main__":
    main()
