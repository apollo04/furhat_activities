import { createContext, useContext, useState } from 'react';

interface RobotContextProps {
  robotInfo: {
    ip: string;
    name: string;
  };
  handleSetRobotInfo: ({ ip, name }: { ip: string; name: string }) => void;
}

const RobotContext = createContext<RobotContextProps | undefined>(undefined);
export const useRobot = () => {
  const context = useContext(RobotContext);
  if (!context) {
    throw new Error('useRobot must be used within a RobotProvider');
  }
  return context;
};

export const RobotProvider = (props: any): JSX.Element => {
  const [robotInfo, setRobotInfo] = useState({
    ip: '',
    name: '',
  });

  const handleSetRobotInfo = ({ ip, name }: { ip: string; name: string }) => {
    setRobotInfo({ ip, name });
  };

  return (
    <RobotContext.Provider
      value={{
        robotInfo,
        handleSetRobotInfo,
      }}
      {...props}
    />
  );
};
