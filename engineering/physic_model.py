from OMPython import ModelicaSystem
import matplotlib.pyplot as plt

file = "/usr/share/doc/omc/testmodels/BouncingBall.mo"
#file = omc.sendExpression("getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\"")
print(file)

package = "BouncingBall"
mod = ModelicaSystem(file, package)
mod.setSimulationOptions(stopTime=3.0, tolerance=1e-08)

mod.simulate()
print(mod.getQuantities())

time, height = mod.getSolutions("time", "h")

plt.plot(time, height)
plt.xlabel('time (s)')
plt.ylabel('height of falling (m)')
plt.show()


# mod.setLinearizationOptions(stopTime=2.0, tolerance=1e-06)
# mod.linearize()
# print(mod.getLinearInputs())
# print(mod.getLinearOutputs())
# print(mod.getLinearStates())
