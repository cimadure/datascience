# from OMPython import OMCSessionZMQ
#
# omc = OMCSessionZMQ()
# print(omc.sendExpression("getVersion()"))
#
# omc.sendExpression("loadModel(Modelica)")
# omc.sendExpression("loadFile(getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\")")
# omc.sendExpression("instantiateModel(BouncingBall)")
# print(omc.sendExpression("getClassNames()"))
#
# cmds = [
#     "loadModel(Modelica)",
#     "model test end test;",
#     'loadFile(getInstallationDirectoryPath() + "/share/doc/omc/testmodels/BouncingBall.mo")',
#     "simulate(BouncingBall)",
#     "plot(h)"
# ]
# # for cmd in cmds:
# #     answer = omc.sendExpression(cmd)
# #     print("\n{}:\n{}".format(cmd, answer))


from OMPython import ModelicaSystem
file = "/usr/share/doc/omc/testmodels/BouncingBall.mo"
#file = omc.sendExpression("getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\"")
print(file)
package = "BouncingBall"
mod = ModelicaSystem(file, package)
mod.setSimulationOptions(stopTime=3.0, tolerance=1e-08)

mod.simulate()
print(mod.getQuantities())

time, height = mod.getSolutions("time", "h")

import matplotlib.pyplot as plt
plt.plot(time, height)
plt.xlabel('time (s)')
plt.ylabel('height of falling (m)')
plt.show()


# mod.setLinearizationOptions(stopTime=2.0, tolerance=1e-06)
# mod.linearize()
# print(mod.getLinearInputs())
# print(mod.getLinearOutputs())
# print(mod.getLinearStates())
